import DataHazardUnit

class EX:
    def __init__(self):
        self.branch_flag = False
        self.update_PC = None
        
    def calculate(self, ID_EX, EX_MEM, MEM_WB, reg, instructionMem):    

        forward_flag = DataHazardUnit.forwarding(ID_EX, EX_MEM, MEM_WB)
        if(forward_flag == 'EX_hazard_rs'):
            result_rs = EX_MEM.result
            result_rt = reg[ID_EX.rt]
        elif(forward_flag == 'EX_hazard_rt'):
            result_rs = reg[ID_EX.rs]
            result_rt = EX_MEM.result
        elif(forward_flag == 'MEM_hazard_rs'):
            result_rs = MEM_WB.result
            result_rt = reg[ID_EX.rt]
        elif(forward_flag == 'MEM_hazard_rt'):
            result_rs = reg[ID_EX.rs]
            result_rt = MEM_WB.result
        else:
            result_rs = reg[ID_EX.rs]
            result_rt = reg[ID_EX.rt]

        if ID_EX.opcode == 'add':
            calculate_result = result_rs + result_rt
            return calculate_result
        elif ID_EX.opcode == 'sub':
            calculate_result = result_rs - result_rt
            return calculate_result
        elif ID_EX.opcode == 'beq':
            rs = ID_EX.rs
            rt = ID_EX.rt
            index = ID_EX.index
            if result_rs == result_rt:
                #因為predict not taken 所以預測錯誤
                self.branch_flag = True         #告知CPU判斷要換PC
                self.update_PC = instructionMem.index(str(ID_EX)) + index + 1  #先將PC存起來
            return None
                
        else:
            pass
            return
        
    def run(self, ID_EX, EX_MEM, MEM_WB, reg, instructionMem):
        self.branch_flag = False
        self.update_PC = None

        if ID_EX:
            calculate_result = self.calculate(ID_EX, EX_MEM, MEM_WB, reg, instructionMem)
            self.EX_MEM = ID_EX
            self.EX_MEM.result = calculate_result

            print(f"EX stage... {self.EX_MEM} {self.EX_MEM.getSignal('EX')}")
        else:
            self.EX_MEM = None
            print(f"EX stage... {self.EX_MEM}")

        return self.EX_MEM