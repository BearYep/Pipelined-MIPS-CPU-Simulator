class MEM:
    def __init__(self):
        pass
    
    def run(self, EX_MEM, mem, reg):
        if EX_MEM:

            if EX_MEM.opcode == 'lw':
                rt = EX_MEM.rt
                offset = EX_MEM.offset
                rs = EX_MEM.rs
                EX_MEM.result = mem[int((offset/4)) + rs]
            elif EX_MEM.opcode == 'sw':
                rt = EX_MEM.rt
                offset = EX_MEM.offset
                rs = EX_MEM.rs
                mem[int((offset/4)) + rs] = reg[rt]
            
            self.MEM_WB = EX_MEM
            
            if EX_MEM.opcode == 'lw': EX_MEM.signal = '010 11'
            elif EX_MEM.opcode == 'sw': EX_MEM.signal = '001 0X'
            elif EX_MEM.opcode == 'add' or EX_MEM.opcode == 'sub': EX_MEM.signal = '000 10'
            elif EX_MEM.opcode == 'beq': EX_MEM.signal = '100 0X'
            
            print(f"MEM stage... {self.MEM_WB} {self.MEM_WB.signal}")
        else:
            self.MEM_WB = None
            print(f"MEM stage... {self.MEM_WB}")

        return self.MEM_WB