class WB:
    def __init__(self):
        pass

    def run(self, MEM_WB, reg):

        if MEM_WB:
            
            if MEM_WB.opcode == 'lw':
                reg[MEM_WB.rt] = MEM_WB.result
            elif MEM_WB.opcode == 'add' or MEM_WB.opcode == 'sub':
                reg[MEM_WB.rd] = MEM_WB.result

            print(f"WB stage... {MEM_WB} {MEM_WB.getSignal('WB')}")
            with open ('result.txt','a') as file:
                file.write(f"WB stage... {MEM_WB} {MEM_WB.getSignal('WB')}\n")
            return MEM_WB
        else:
            print("WB stage... None")
            with open ('result.txt','a') as file:
                file.write("WB stage... None\n")