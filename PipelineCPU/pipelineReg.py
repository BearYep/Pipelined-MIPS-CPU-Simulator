class pipelineRegister:

    opcode = None
    rd = None
    rs = None
    rt = None
    index = None
    offset = None
    base = None

    def __init__(self, op, num1, num2, num3):
        if op == "lw" or op == "sw":
            self.opcode = op
            self.rt = num1
            self.offset = num2
            self.rs = num3
        elif op == "add" or op == "sub":
            self.opcode = op
            self.rd = num1
            self.rs = num2
            self.rt = num3
        else:   #beq
            self.opcode = op
            self.rs = num1
            self.rt = num2
            self.index = num3

    def __str__(self):
        if self.opcode == "lw" or self.opcode == "sw":
            return f"{self.opcode} ${self.rt}, {self.offset}(${self.rs})"
        elif self.opcode == "add" or self.opcode == "sub":
            return f"{self.opcode} ${self.rd}, ${self.rs}, ${self.rt}"
        elif self.opcode == "beq":
            return f"{self.opcode} ${self.rs}, ${self.rt}, ${self.index}"
        else:
            return "invalid instruction"   