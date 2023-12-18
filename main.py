import re

reg = [1] * 32 #length = 32 , per length 1 words
reg[0] = 0
mem = [1] * 32 #length = 32 , per length 1 words
print(reg)
print(mem)

class regIns:
    def __init__(self, op, num1, num2, num3):
        if op == "lw" or op == "sw":
            self.op = op
            self.rd = num1
            self.offset = num2
            self.base = num3

            self.rs = None
            self.rt = None
            self.index = None
        elif op == "add" or op == "sub":
            self.op = op
            self.rd = num1
            self.rs = num2
            self.rt = num3

            self.offset = None
            self.base = None
            self.index = None
        else:   #beq
            self.op = op
            self.rs = num1
            self.rt = num2
            self.index = num3

            self.offset = None
            self.base = None
            self.rd = None

    def __str__(self):
        if self.op == "lw" or self.op == "sw":
            return f"{self.op} ${self.rd}, {self.offset}(${self.base})"
        elif self.op == "add" or self.op == "sub":
            return f"{self.op} ${self.rd}, ${self.rs}, ${self.rt}"
        elif self.op == "beq":
            return f"{self.op} ${self.rs}, ${self.rt}, ${self.index}"
        else:
            return "invalid instruction"       


class CPU:

    def __init__(self):

        self.IF_ID = None
        self.ID_EX = None
        self.EX_MEM = None
        self.MEM_WB = None

        self.instuction_mem = []
        self.cycle = 0


    # def readInstruction(self, ins):
    #     self.instuction_mem = ins
    
    def calculate(self):    #do what opcode want (should write in exe?，get more info from stage and calculate)

        matches = re.findall(r'\d+', self.instuction_mem[0])    #split num out (no need)

        if(self.instuction_mem[0].split()[0]) == 'lw':
            rd = int(matches[0])
            offset = int(matches[1])
            base = int(matches[2])
            reg[rd] = mem[int((offset/4)) + base]
        elif(self.instuction_mem[0].split()[0]) == 'sw':
            rd = int(matches[0])
            offset = int(matches[1])
            base = int(matches[2])
            mem[int((offset/4)) + base] = reg[rd]
        elif(self.instuction_mem[0].split()[0]) == 'add':
            rd = int(matches[0])
            rs = int(matches[1])
            rt = int(matches[2])
            reg[rd] = reg[rs] + reg[rt]
        elif(self.instuction_mem[0].split()[0]) == 'sub':
            rd = int(matches[0])
            rs = int(matches[1])
            rt = int(matches[2])
            reg[rd] = reg[rs] - reg[rt]
        elif(self.instuction_mem[0].split()[0]) == 'beq':
            pass
        else:
            print("error")
            return

    def IF(self):
        if self.instuction_mem:
            matches = re.findall(r'\d+', self.instuction_mem[0])
            opcode = self.instuction_mem[0].split()[0]
            self.IF_ID = regIns(opcode, int(matches[0]), int(matches[1]), int(matches[2]))
            #self.IF_ID = self.instuction_mem[0]
            #self.calculate()
        
        print(f"IF stage... {self.IF_ID}")

    def ID(self):
        if self.IF_ID:
            self.ID_EX = self.IF_ID
            self.IF_ID = None
        print(f"ID stage... {self.ID_EX}")

    def EX(self):
        if self.ID_EX:
            self.EX_MEM = self.ID_EX
            self.ID_EX = None
        print(f"EX stage... {self.EX_MEM}")

    def MEM(self):
        if self.EX_MEM:
            self.MEM_WB = self.EX_MEM
            self.EX_MEM = None
        print(f"MEM stage... {self.MEM_WB}")

    def WB(self):
        if self.MEM_WB:
            print(f"WB stage... {self.MEM_WB}")
            self.MEM_WB = None
        else:
            print("WB stage... None")
    
    def run(self, ins):
        self.instuction_mem = ins
        while self.instuction_mem or self.IF_ID or self.ID_EX or self.EX_MEM or self.MEM_WB:
            self.cycle = self.cycle + 1
            print(f'Cycle {self.cycle}')
            self.WB()
            self.MEM()
            self.EX()
            self.ID()
            self.IF()
            if self.instuction_mem:
                del self.instuction_mem[0]
            
            
            
app = CPU()

def main():
    path = './input/test1.txt'
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    print(lines)
    #app.readInstruction(lines)
    # for line in lines:
        # app.readInstruction(line)
        # app.run()
    app.run(lines)
    print(reg)
    print(mem)
    f.close()

if __name__ == "__main__":
    main()
