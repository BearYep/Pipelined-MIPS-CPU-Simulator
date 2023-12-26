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
            
            print(f"MEM stage... {self.MEM_WB} {self.MEM_WB.getSignal('MEM')}")
        else:
            self.MEM_WB = None
            print(f"MEM stage... {self.MEM_WB}")

        return self.MEM_WB