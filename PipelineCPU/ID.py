class ID:
    def __init__(self):
        pass

    def run(self, IF_ID, temp_mem, temp_reg, mem, reg):
        if IF_ID:
            self.ID_EX = IF_ID
            if IF_ID.opcode == "beq":   #判斷到beq時先將目前的reg,mem存下，以免預測錯誤
                for i in range (len(reg)):
                    temp_reg[i] = reg[i]
                for i in range (len(mem)):
                    temp_mem[i] = mem[i]
        else:
            self.ID_EX = None

        print(f"ID stage... {self.ID_EX}")
        return self.ID_EX