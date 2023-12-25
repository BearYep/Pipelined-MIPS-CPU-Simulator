from PipelineCPU.IF import IF
from PipelineCPU.ID import ID
from PipelineCPU.EX import EX
from PipelineCPU.MEM import MEM
from PipelineCPU.WB import WB


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

        self.instructionMemory = list()
        

    def run(self, ins):
        self.instructionMemory = ins
        self.cycle = 0

        do_while_flag = True

        while do_while_flag or self.IF_ID or self.ID_EX or self.EX_MEM or self.MEM_WB:
            self.cycle = self.cycle + 1

            # if self.instructionMemory:
            #     print(len(self.instructionMemory))

            print(f'Cycle {self.cycle}')
            #要傳reg和mem給要用的
            self.WB.run(self.MEM_WB)
            self.MEM_WB = self.MEM.run(self.EX_MEM)
            self.EX_MEM = self.EX.run(self.ID_EX, self.mem, self.reg, self.instructionMemory)
            self.ID_EX = self.ID.run(self.IF_ID)
            self.IF_ID = self.IF.run(self.instructionMemory, self.pc)
            self.pc = self.pc + 1
            # if self.instructionMemory:
            #     del self.instructionMemory[0]
            do_while_flag = False

        