class pipelineRegister:

    opcode = None
    rd = None
    rs = None
    rt = None
    index  = None
    offset = None
    result = None

    def __init__(self, op, num1, num2, num3):
        if op == "lw" or op == "sw":
            self.opcode = op
            self.rt = num1
            self.offset = num2
            self.rs = num3  
            self.result = None
        elif op == "add" or op == "sub":
            self.opcode = op
            self.rd = num1
            self.rs = num2
            self.rt = num3
            self.result = None
        else:   #beq
            self.opcode = op
            self.rs = num1
            self.rt = num2
            self.index = num3

    def setSignal(self, signal):
        self.RegDst   = int(signal[0]) if signal[0] != 'X' else 'X'
        self.ALUSrc   = int(signal[1])
        self.Branch   = int(signal[2])
        self.MemRead  = int(signal[3])
        self.MemWrite = int(signal[4])
        self.RegWrite = int(signal[5])
        self.MemtoReg = int(signal[6]) if signal[6] != 'X' else 'X'

    @property
    def signal(self):
        return (f'{self.RegDst}{self.ALUSrc} {self.Branch}{self.MemRead}{self.MemWrite} {self.RegWrite}{self.MemtoReg}')
    
    def getSignal(self, Stage):
        if Stage == 'EX':
            return (f'{self.RegDst}{self.ALUSrc} {self.Branch}{self.MemRead}{self.MemWrite} {self.RegWrite}{self.MemtoReg}')
        elif Stage == 'MEM':
            return (f'{self.Branch}{self.MemRead}{self.MemWrite} {self.RegWrite}{self.MemtoReg}')
        elif Stage == 'WB':
            return (f'{self.RegWrite}{self.MemtoReg}')
    
    def __str__(self):
        if self.opcode == "lw" or self.opcode == "sw":
            return f"{self.opcode} ${self.rt}, {self.offset}(${self.rs})"
        elif self.opcode == "add" or self.opcode == "sub":
            return f"{self.opcode} ${self.rd}, ${self.rs}, ${self.rt}"
        elif self.opcode == "beq":
            return f"{self.opcode} ${self.rs}, ${self.rt}, {self.index}"
        else:
            return "invalid instruction"   