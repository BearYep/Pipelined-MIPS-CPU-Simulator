reg = [] #length = 32 , per length 1 words
mem = [] #length = 32 , per length 1 words

class CPU:
    def __init__(self):
        self.IF_ID = []
        self.ID_EX = []
        self.EX_MEM = []
        self.MEM_WB = []

    def readInstruction(self, ins):
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

app = CPU()

def main():
    path = 'text.txt'
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    print(lines)
    for line in lines:
        app.readInstruction(line)
    f.close()

if __name__ == "__main__":
    main()