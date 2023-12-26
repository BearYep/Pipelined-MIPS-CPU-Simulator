class WB:
    def __init__(self):
        pass

    def run(self, MEM_WB, mem, reg):

        if MEM_WB:
            
            if MEM_WB.opcode == 'lw':
                reg[MEM_WB.rt] = MEM_WB.result
            elif MEM_WB.opcode == 'add' or MEM_WB.opcode == 'sub':
                reg[MEM_WB.rd] = MEM_WB.result

            if MEM_WB.opcode == 'lw': MEM_WB.signal = '11'
            elif MEM_WB.opcode == 'sw': MEM_WB.signal = '0X'
            elif MEM_WB.opcode == 'add' or MEM_WB == 'sub': MEM_WB.signal = '10'
            elif MEM_WB.opcode == 'beq': MEM_WB.signal = '0X'

            print(f"WB stage... {MEM_WB} {MEM_WB.signal}")
        else:
            print("WB stage... None")