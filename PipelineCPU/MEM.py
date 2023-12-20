class MEM:
    def __init__(self):
        pass
    
    def run(self, EX_MEM):
        if EX_MEM:
            self.MEM_WB = EX_MEM
        else:
            self.MEM_WB = None

        print(f"MEM stage... {self.MEM_WB}")
        return self.MEM_WB