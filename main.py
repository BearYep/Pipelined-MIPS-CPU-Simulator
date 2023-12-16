reg = [] #length = 32 , per length 1 words
mem = [] #length = 32 , per length 1 words

class CPU:
    def __init__(self):

        self.IF_ID = []
        self.ID_EX = []
        self.EX_MEM = []
        self.MEM_WB = []

        self.instuction_mem = []
        self.cycle = 0


    def readInstruction(self, ins):
        self.instuction_mem = ins
        if(ins.split()[0]) == 'lw':
            pass
            #opcode、read reg 
        elif(ins.split()[0]) == 'sw':
            pass
        elif(ins.split()[0]) == 'add':
            pass
        elif(ins.split()[0]) == 'sub':
            pass
        elif(ins.split()[0]) == 'beq':
            pass
        else:
            print("error")
            return
        
        print(ins.split())
    
    def IF(self):
        self.IF_ID = self.instuction_mem
        print("IF stage...")
    def ID(self):
        if self.IF_ID:
            self.ID_EX = self.IF_ID
            self.IF_ID = None
    def EXE(self):
        pass
    def MEM(self):
        pass
    def WB(self):
        pass
    
    def run(self):
        while self.instuction_mem or self.IF_ID or self.ID_EX or self.EX_MEM or self.MEM_WB:
            self.IF()
            self.ID()
            self.EXE()
            self.MEM()
            self.WB()
            
app = CPU()

def main():
    path = './input/test1.txt'
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    print(lines)
    for line in lines:
        app.readInstruction(line)
        app.run()
    f.close()

if __name__ == "__main__":
    main()
