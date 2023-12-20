import re
from PipelineCPU.pipelineReg import pipelineRegister

class IF:
    def __init__(self):
        pass
    
    def run(self, instructionMem):
        if instructionMem: #判斷IF要不要作動
            matches = re.findall(r'\d+', instructionMem[0])
            print(matches)
            opcode = instructionMem[0].split()[0]
            self.IF_ID = pipelineRegister(opcode, int(matches[0]), int(matches[1]), int(matches[2]))
               
        else:
            self.IF_ID = None
            
        print(f"IF stage... {self.IF_ID}")
        return self.IF_ID
        
        