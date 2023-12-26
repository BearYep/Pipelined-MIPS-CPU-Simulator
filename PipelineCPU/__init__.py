from PipelineCPU.IF import IF
from PipelineCPU.ID import ID
from PipelineCPU.EX import EX
from PipelineCPU.MEM import MEM
from PipelineCPU.WB import WB
# from DataHazardUnit import Data_Hazard


class CPU:


    def __init__(self):
        self.reg = [1] * 32 #length = 32 , per length 1 words
        self.reg[0] = 0
        self.mem = [1] * 32 #length = 32 , per length 1 words
        self.pc = 0

        self.IF_ID = None
        self.ID_EX = None
        self.EX_MEM = None
        self.MEM_WB = None

        self.IF = IF()
        self.ID = ID()
        self.EX = EX()
        self.MEM = MEM()
        self.WB = WB()

        self.instruction_memory: list()
        # self.data_hazard_unit = Data_Hazard()
        

    def run(self, ins):
        self.instruction_memory = ins
        cycle = 0
        
        while True:
            cycle += 1
            # if self.instruction_memory:
            #     print(len(self.instruction_memory))

            print(f'Cycle {cycle}')
            #要傳reg和mem給要用的
            self.WB.run(self.MEM_WB, self.mem, self.reg)
            self.MEM_WB = self.MEM.run(self.EX_MEM, self.mem, self.reg)
            self.EX_MEM = self.EX.run(self.ID_EX, self.pc, self.reg, self.instruction_memory)
            
            #EX有沒有做事 AND 做完(beq)之後有沒有預測有沒有錯 =True=> pass ID、改新PC
            if(self.EX_MEM and self.EX.branch_flag):
                self.pc = self.EX.update_PC
                self.ID_EX = None
            else:
                self.ID_EX = self.ID.run(self.IF_ID)

            self.IF_ID  = self.IF.run(self.instruction_memory, self.pc)
            self.pc += 1 
            # if self.instruction_memory:
            #     del self.instruction_memory[0]
            if not(self.IF_ID or self.ID_EX or self.EX_MEM or self.MEM_WB):
                break
        
