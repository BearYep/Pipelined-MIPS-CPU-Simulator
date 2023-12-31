from PipelineCPU.IF import IF
from PipelineCPU.ID import ID
from PipelineCPU.EX import EX
from PipelineCPU.MEM import MEM
from PipelineCPU.WB import WB
import HazardUnit
from PipelineCPU.ForwardingUnit import ForwardingUnit


class CPU:

    reg = [1] * 32 #length = 32 , per length 1 words
    reg[0] = 0
    mem = [1] * 32 #length = 32 , per length 1 words

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
        self.result: list()

    def run(self, ins):
        self.instruction_memory = ins
        cycle = 0

        stall_beq = False
        beq_count = 0

        self.result = []

        while True:
            stall = False
            cycle += 1

            # if self.instruction_memory:
            #     print(len(self.instruction_memory))

            print(f'Cycle {cycle}')
            #要傳reg和mem給要用的
            self.WB.run(self.MEM_WB, self.reg)
            self.MEM_WB = self.MEM.run(self.EX_MEM, self.mem, self.reg)

            self.EX_MEM = self.EX.run(self.ID_EX, self.EX_MEM, self.MEM_WB, self.reg, self.instruction_memory)
            
            # print(self.EX.branch_flag)
            #EX有沒有做事 AND 做完(beq)之後有沒有預測有沒有錯 =True=> pass ID、改新PC
            if(self.EX_MEM and self.EX.branch_flag):
                self.pc = self.EX.update_PC
                self.IF_ID = HazardUnit.NOP()
                #stall = True
            # elif(DataHazardUnit.load_use_hazard(self.IF_ID, self.ID_EX) and beq_count == 0):
            #     if(self.IF_ID.opcode == 'beq'):
            #         #wait 2 cycle
            #         self.ID.run(self.IF_ID, self.reg, self.instruction_memory)
            #         stall = True
            #         stall_beq = True
            #         self.ID_EX = None
            # else:
            #     self.ID.run(self.IF_ID, self.ID_EX, self.EX_MEM, self.MEM_WB, self.reg, self.instruction_memory)
            #     self.ID_EX = None
                 
            if(HazardUnit.load_use_hazard(self.IF_ID, self.ID_EX)):
                stall = True
            condition = HazardUnit.branch_hazard(self.IF_ID, self.ID_EX, self.EX_MEM, self.MEM_WB, ForwardingUnit())
            if(condition == 0b10):
                stall = True
            elif(condition == 0b11):
                stall_beq = True
            if(stall or stall_beq):
                self.ID.run(self.IF_ID, self.ID_EX, self.EX_MEM, self.MEM_WB, self.reg, self.instruction_memory)
                if(self.EX.branch_flag):
                    self.IF_ID = self.IF.run(self.instruction_memory, self.pc)
                else:
                    self.IF.run(self.instruction_memory, self.pc)
                    self.pc -= 1
                
                self.ID_EX = HazardUnit.NOP()
            else:
                self.ID_EX = self.ID.run(self.IF_ID, self.ID_EX, self.EX_MEM, self.MEM_WB, self.reg, self.instruction_memory)
                self.IF_ID = self.IF.run(self.instruction_memory, self.pc)

            if(stall_beq):
                beq_count += 1

            if(beq_count == 2):
                beq_count = 0
                stall_beq = False

            self.pc += 1
            # if self.instruction_memory:
            #     del self.instruction_memory[0]
            if not(self.IF_ID or self.ID_EX or self.EX_MEM or self.MEM_WB):
                with open ('result.txt', 'a') as file: 
                    file.write('Final Registers: {}\n'.format(self.reg))
                    file.write('Final Memory: {}\n'.format(self.mem))
                    file.write(f'Need {self.pc} cycles')
                break