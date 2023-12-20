from PipelineCPU.IF import IF
from PipelineCPU.ID import ID
from PipelineCPU.EX import EX
from PipelineCPU.MEM import MEM
from PipelineCPU.WB import WB


class CPU:

    reg = [1] * 32 #length = 32 , per length 1 words
    reg[0] = 0
    mem = [1] * 32 #length = 32 , per length 1 words

    def __init__(self):
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
        while self.instructionMemory or self.IF_ID or self.ID_EX or self.EX_MEM or self.MEM_WB:
            self.cycle = self.cycle + 1
            print(f'Cycle {self.cycle}')
            self.WB.run(self.MEM_WB)
            self.MEM_WB = self.MEM.run(self.EX_MEM)
            self.EX_MEM = self.EX.run(self.ID_EX)
            self.ID_EX = self.ID.run(self.IF_ID)
            self.IF_ID = self.IF.run(self.instructionMemory)
            if self.instructionMemory:
                del self.instructionMemory[0]