reg = [1] * 32 #length = 32 , per length 1 words
reg[0] = 0
mem = [1] * 32 #length = 32 , per length 1 words
print(reg)
print(mem)

class CPU:
    def __init__(self):

        self.IF_ID = None
        self.ID_EX = None
        self.EX_MEM = None
        self.MEM_WB = None

        self.instuction_mem = []
        self.cycle = 0


    def readInstruction(self, ins):
        self.instuction_mem = ins
        if(ins[0].split()[0]) == 'lw':
            pass
            #opcode、read reg 
        elif(ins[0].split()[0]) == 'sw':
            pass
        elif(ins[0].split()[0]) == 'add':
            pass
        elif(ins[0].split()[0]) == 'sub':
            pass
        elif(ins[0].split()[0]) == 'beq':
            pass
        else:
            print("error")
            return
        
        print(ins[0].split())
    
    def IF(self):
        if self.instuction_mem:
            self.IF_ID = self.instuction_mem[0]
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
    
    def run(self):
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
    app.readInstruction(lines)
    # for line in lines:
        # app.readInstruction(line)
        # app.run()
    app.run()
    f.close()

if __name__ == "__main__":
    main()
