import re
from PipelineCPU.pipelineReg import pipelineRegister

def divide_ins(instruction):
    parts = instruction.split(' ')
    if(parts[0] == 'lw' or parts[0] == 'sw'):
        opcode = parts[0]

        matches = re.findall(r'\d+', parts[1])
        num1 = matches[0]
    
        matches = re.findall(r'\d+', parts[2])
        num2 = matches[0]
        num3 = matches[1]

    elif(parts[0] == 'add' or parts[0] == 'sub'):
        matches = re.findall(r'\d+', instruction)
        opcode = parts[0]
        num1 = matches[0]
        num2 = matches[1]
        num3 = matches[2]

    elif(parts[0] == 'beq'):
        opcode = parts[0]
        num1, num2, num3 = re.findall(r'-?\d+', instruction)
    
    return opcode, num1, num2, num3



class IF:
    def __init__(self):
        pass
    
    def run(self, instructionMem, pc):
        if len(instructionMem) > pc:
            code = divide_ins(instructionMem[pc])
            self.IF_ID = pipelineRegister(code[0], int(code[1]), int(code[2]), int(code[3]))
        else:
            self.IF_ID = None
        
        
        print(f"IF stage... {self.IF_ID}")
        with open ('result.txt','a') as file:
            file.write(f"IF stage... {self.IF_ID}\n")
        return self.IF_ID