import re

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

        #matches = re.findall(r'\d+', self.instructionMemory)
        matches = re.findall(r'\d+', str(IF_ID))
        opcode = IF_ID.opcode

        if opcode == 'lw':
            IF_ID.rd = int(matches[0])
            IF_ID.offset = int(matches[1])
            IF_ID.base = int(matches[2])
            IF_ID.signal = '01 010 11'

        elif opcode == 'sw':
            IF_ID.rd = int(matches[0])
            IF_ID.offset = int(matches[1])
            IF_ID.base = int(matches[2])
            IF_ID.signal = 'X1 001 0X'

        elif opcode == 'add':
            IF_ID.rd = int(matches[0])
            IF_ID.rs = int(matches[1])
            IF_ID.rt = int(matches[2])
            IF_ID.signal = '10 000 10'

        elif opcode == 'sub':
            IF_ID.rd = int(matches[0])
            IF_ID.rs = int(matches[1])
            IF_ID.rt = int(matches[2])
            IF_ID.signal = '10 000 10'

        elif opcode == 'beq':
            IF_ID.rs = int(matches[0])
            IF_ID.rt = int(matches[1])
            IF_ID.offset = int(matches[2])
            IF_ID.signal = 'X0 100 0X'

        else:
            print("error")
            return
