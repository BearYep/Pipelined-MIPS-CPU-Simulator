import PipelineCPU.HazardUnit as HazardUnit
from PipelineCPU.ForwardingUnit import ForwardingUnit

class ID:
    def __init__(self):
        self.stall = False

    def run(self, IF_ID, ID_EX, EX_MEM, MEM_WB, reg, instructionMem):
        if IF_ID:
            self.decode(IF_ID)
            if(IF_ID.opcode == 'beq'):
                self.registerComparator(IF_ID, ID_EX, EX_MEM, MEM_WB, reg, instructionMem)
            if not(self.stall):
                self.ID_EX = IF_ID
            else:
                self.ID_EX = None
        else:
            self.ID_EX = None

        print(f"ID stage... {self.ID_EX}")
        with open ('result.txt', 'a') as file:
            file.write(f"ID stage... {self.ID_EX}\n")
        return self.ID_EX
    
    def decode(self, IF_ID):
        if IF_ID.opcode == 'lw': IF_ID.setSignal('0101011')
        elif IF_ID.opcode == 'sw': IF_ID.setSignal('X10010X')
        elif IF_ID.opcode == 'add': IF_ID.setSignal('1000010')
        elif IF_ID.opcode == 'sub': IF_ID.setSignal('1000010')
        elif IF_ID.opcode == 'beq': IF_ID.setSignal('X01000X')
        else: print("error")
    
    def registerComparator(self, IF_ID, ID_EX, EX_MEM, MEM_WB, reg, instructionMem):
        self.stall = False
        forwardingUnit = ForwardingUnit()
        result_rs = reg[IF_ID.rs]
        result_rt = reg[IF_ID.rt]
        condition = HazardUnit.branch_hazard(IF_ID, ID_EX, EX_MEM, MEM_WB, forwardingUnit)
        if(condition == 0b01):
            if(forwardingUnit.ForwardA == 0b10):
                result_rs = EX_MEM.result
            if(forwardingUnit.ForwardB == 0b10):
                result_rt = EX_MEM.result
            if(forwardingUnit.ForwardA == 0b01):
                result_rs = MEM_WB.result
            if(forwardingUnit.ForwardB == 0b01):
                result_rt = MEM_WB.result
        elif(condition == 0b10):
            if(forwardingUnit.ForwardA == 0b10):
                result_rs = ID_EX.result
            if(forwardingUnit.ForwardB == 0b10):
                result_rt = ID_EX.result
            if(forwardingUnit.ForwardA == 0b01):
                result_rs = EX_MEM.result
            if(forwardingUnit.ForwardB == 0b01):
                result_rt = EX_MEM.result
        elif(condition == 0b11):
            if(forwardingUnit.ForwardA == 0b10):
                result_rs = ID_EX.result
            if(forwardingUnit.ForwardB == 0b10):
                result_rt = ID_EX.result

        if result_rs == result_rt:
            IF_ID.result = instructionMem.index(str(IF_ID)) + IF_ID.index + 1
