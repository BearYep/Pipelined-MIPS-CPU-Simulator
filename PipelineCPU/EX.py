import re

class EX:
    def __init__(self):
        pass

    def calculate(self):    #do what opcode want (should write in exe?，get more info from stage and calculate)

        matches = re.findall(r'\d+', self.instructionMemory[0])    #split num out (no need) #這邊要改ID_EX

        if(self.instructionMemory[0].split()[0]) == 'lw':
            rd = int(matches[0])
            offset = int(matches[1])
            base = int(matches[2])
            self.reg[rd] = self.mem[int((offset/4)) + base]
        elif(self.instructionMemory[0].split()[0]) == 'sw':
            rd = int(matches[0])
            offset = int(matches[1])
            base = int(matches[2])
            self.mem[int((offset/4)) + base] = self.reg[rd]
        elif(self.instructionMemory[0].split()[0]) == 'add':
            rd = int(matches[0])
            rs = int(matches[1])
            rt = int(matches[2])
            self.reg[rd] = self.reg[rs] + self.reg[rt]
        elif(self.instructionMemory[0].split()[0]) == 'sub':
            rd = int(matches[0])
            rs = int(matches[1])
            rt = int(matches[2])
            self.reg[rd] = self.reg[rs] - self.reg[rt]
        elif(self.instructionMemory[0].split()[0]) == 'beq':
            rs = int(matches[0])
            rt = int(matches[1])
            offset = int(matches[2])
            if self.reg[rs] == self.reg[rt]:
                pass
            else:
                pass
        else:
            print("error")
            return
        
    def run(self, ID_EX):

        if ID_EX:
            # self.calculate()
            self.EX_MEM = ID_EX
        else:
            self.EX_MEM = None

        print(f"EX stage... {self.EX_MEM}")
        return self.EX_MEM
    
        

