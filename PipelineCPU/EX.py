import PipelineCPU.HazardUnit as HazardUnit
from PipelineCPU.ForwardingUnit import ForwardingUnit

class EX:
    def __init__(self):
        self.branch_flag = False
        self.update_PC = None
        
    def calculate(self, ID_EX, EX_MEM, MEM_WB, reg, instructionMem, forwardingUnit):    
        result_rs = reg[ID_EX.rs]
        result_rt = reg[ID_EX.rt]
        HazardUnit.detect_Hazard(ID_EX, EX_MEM, MEM_WB, forwardingUnit)
        if(forwardingUnit.ForwardA == 0b10 and EX_MEM):
            result_rs = EX_MEM.result
        if(forwardingUnit.ForwardB == 0b10 and EX_MEM):
            result_rt = EX_MEM.result
        if(forwardingUnit.ForwardA == 0b01 and MEM_WB):
            result_rs = MEM_WB.result
        if(forwardingUnit.ForwardB == 0b01 and MEM_WB):
            result_rt = MEM_WB.result
        
        if ID_EX.opcode == 'add':
            calculate_result = result_rs + result_rt
            return calculate_result
        elif ID_EX.opcode == 'sub':
            calculate_result = result_rs - result_rt
            return calculate_result
        elif ID_EX.opcode == 'beq':

            if ID_EX.result:
                self.branch_flag = True 
                self.update_PC = ID_EX.result 
        else:
            pass
            return
        
    def run(self, ID_EX, EX_MEM, MEM_WB, reg, instructionMem):
        self.branch_flag = False
        self.update_PC = None
        

        if ID_EX:
            self.forwardingUnit = ForwardingUnit()
            calculate_result = self.calculate(ID_EX, EX_MEM, MEM_WB, reg, instructionMem, self.forwardingUnit)
            
            self.EX_MEM = ID_EX
            self.EX_MEM.result = calculate_result
            print(f"EX stage... {self.EX_MEM} {self.EX_MEM.getSignal('EX')}")
            with open('result.txt' ,'a') as file:
                file.write(f"EX stage... {self.EX_MEM} {self.EX_MEM.getSignal('EX')}\n")
        else:
            self.EX_MEM = None
            print(f"EX stage... {self.EX_MEM}")
            with open('result.txt' ,'a') as file:
                file.write(f"EX stage... {self.EX_MEM}\n")

        return self.EX_MEM