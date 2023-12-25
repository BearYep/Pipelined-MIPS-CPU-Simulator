class MEM:
    def __init__(self):
        pass
    
    def run(self, EX_MEM):
        if EX_MEM:
            self.MEM_WB = EX_MEM
            
            if EX_MEM.opcode == 'lw': 
                EX_MEM.signal = '010 11'
            elif EX_MEM.opcode == 'sw': 
                EX_MEM.signal = '001 0X'
            elif EX_MEM.opcode == 'add' or EX_MEM.opcode == 'sub': 
                EX_MEM.signal = '000 10'
            elif EX_MEM.opcode == 'beq': 
                EX_MEM.signal = '100 0X'
            print(f"MEM stage... {self.MEM_WB} {EX_MEM.signal}")
        else:
            self.MEM_WB = None
            print(f"MEM stage... {self.MEM_WB}")

        return self.MEM_WB