import re

class EX:
    def __init__(self, mem, reg):
        self.mem = mem
        self.reg = reg

    def calculate(self, ID_EX):    #do what opcode want (should write in exe?，get more info from stage and calculate)

        if ID_EX.opcode == 'lw':
            self.reg[ID_EX.rd] = self.mem[int((ID_EX.offset/4)) + ID_EX.base]

        elif ID_EX.opcode == 'sw':
            self.mem[int((ID_EX.offset/4)) + ID_EX.base] = self.reg[ID_EX.rd]

        elif ID_EX.opcode == 'add':
            self.reg[ID_EX.rd] = self.reg[ID_EX.rs] + self.reg[ID_EX.rt]
            
        elif ID_EX.opcode == 'sub':
            self.reg[ID_EX.rd] = self.reg[ID_EX.rs] - self.reg[ID_EX.rt]

        elif ID_EX.opcode == 'beq':
            if self.reg[ID_EX.rs] == self.reg[ID_EX.rt]:
                pass
            else:
                pass

        else:
            print("error")
            return
        
    def run(self, ID_EX):

        if ID_EX:
            self.calculate(ID_EX)
            self.EX_MEM = ID_EX

            print(f"EX stage... {self.EX_MEM} {self.EX_MEM.signal}")
        else:
            self.EX_MEM = None
            print(f"EX stage... {self.EX_MEM}")

        print(f"EX stage... {self.EX_MEM}")
        return self.EX_MEM
    
        

