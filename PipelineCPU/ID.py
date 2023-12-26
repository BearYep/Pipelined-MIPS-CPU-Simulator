class ID:
    def __init__(self):
        pass

    def run(self, IF_ID):
        if IF_ID:
            self.decode(IF_ID)
            self.ID_EX = IF_ID
        else:
            self.ID_EX = None

        print(f"ID stage... {self.ID_EX}")
        return self.ID_EX
    
    def decode(self, IF_ID):

        if IF_ID.opcode == 'lw': IF_ID.setSignal('0101011')
        elif IF_ID.opcode == 'sw': IF_ID.setSignal('X10010X')
        elif IF_ID.opcode == 'add': IF_ID.setSignal('1000010')
        elif IF_ID.opcode == 'sub': IF_ID.setSignal('1000010')
        elif IF_ID.opcode == 'beq': IF_ID.setSignal('X01000X')
        else: print("error")

        # print(IF_ID.signal)