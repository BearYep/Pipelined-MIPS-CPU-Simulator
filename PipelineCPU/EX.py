import re

class EX:
    def __init__(self, mem, reg):
        self.mem = mem
        self.reg = reg

    def calculate(self, ID_EX, temp_mem, temp_reg, mem, reg, instructionMem):    

        if ID_EX.opcode == 'lw':
            rs = ID_EX.rs
            offset = ID_EX.offset
            base = ID_EX.base
            reg[rs] = mem[int((offset/4)) + base]
        elif ID_EX.opcode == 'sw':
            rs = ID_EX.rs
            offset = ID_EX.offset
            base = ID_EX.base
            mem[int((offset/4)) + base] = reg[rs]
        elif ID_EX.opcode == 'add':
            rd = ID_EX.rd
            rs = ID_EX.rs
            rt = ID_EX.rt
            reg[rd] = reg[rs] + reg[rt]
        elif ID_EX.opcode == 'sub':
            rd = ID_EX.rd
            rs = ID_EX.rs
            rt = ID_EX.rt
            reg[rd] = reg[rs] - reg[rt]
        elif ID_EX.opcode == 'beq':
            rs = ID_EX.rs
            rt = ID_EX.rt
            index = ID_EX.index
            if reg[rs] == reg[rt]:
                #因為predict not taken 所以預測錯誤
                #跳傳branch到的指令 並吃下個指令
                #...
                #把預測結果出來前所吃進reg和mem的資料重置到原本狀態
                for i in range (len(reg)):
                    reg[i] = temp_reg[i]
                for i in range (len(mem)):
                    mem[i] = temp_mem[i]
        else:
            print("error")
            return
        
    def run(self, ID_EX, temp_mem, temp_reg, mem, reg, instructionMem):

        if ID_EX:
            self.calculate(ID_EX, temp_mem, temp_reg, mem, reg, instructionMem)
            self.EX_MEM = ID_EX

            print(f"EX stage... {self.EX_MEM} {self.EX_MEM.signal}")
        else:
            self.EX_MEM = None
            print(f"EX stage... {self.EX_MEM}")

        print(f"EX stage... {self.EX_MEM}")
        return self.EX_MEM
    
        

