class EX:
    def __init__(self):
        self.update_PC = None

    def calculate(self, ID_EX, pc, reg, instructionMem):    

        if ID_EX.opcode == 'add':
            rs = ID_EX.rs
            rt = ID_EX.rt
            calculate_result = reg[rs] + reg[rt]
            return calculate_result
        elif ID_EX.opcode == 'sub':
            rs = ID_EX.rs
            rt = ID_EX.rt
            calculate_result = reg[rs] - reg[rt]
            return calculate_result
        elif ID_EX.opcode == 'beq':
            rs = ID_EX.rs
            rt = ID_EX.rt
            index = ID_EX.index
            if reg[rs] == reg[rt]:
                #因為predict not taken 所以預測錯誤
                self.branch_flag = True         #告知CPU判斷要換PC
                self.update_PC = instructionMem.index(str(ID_EX)) + index + 1  #先將PC存起來
            return None
                
        else:
            pass
            return
        
    def run(self, ID_EX, pc, reg, instructionMem):
        self.branch_flag = False
        self.update_PC = None

        if ID_EX:
            calculate_result = self.calculate(ID_EX, pc, reg, instructionMem)
            self.EX_MEM = ID_EX
            self.EX_MEM.result = calculate_result

            print(f"EX stage... {self.EX_MEM} {self.EX_MEM.getSignal('EX')}")
        else:
            self.EX_MEM = None
            print(f"EX stage... {self.EX_MEM}")

        return self.EX_MEM, self.branch_flag
    
    def getUpdatePC(self):
        return self.update_PC
        

