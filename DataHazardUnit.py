class Data_Hazard:

    def detection(self, ID_EX, EX_MEM, MEM_WB):
        if not self.forwarding(ID_EX, EX_MEM, MEM_WB):
            self.NOP()

    def forwarding(self, ID_EX, EX_MEM, MEM_WB):
        # EX hazard
        if EX_MEM.RegWrite and (EX_MEM.rd != 0) and (EX_MEM.rd == ID_EX.rs):
            # Forward to rs
            ID_EX = EX_MEM

        if EX_MEM.RegWrite and (EX_MEM.rd != 0) and (EX_MEM.rs == ID_EX.rt):
            # Forward to rt
            ID_EX = EX_MEM

        # MEM hazard
        if MEM_WB.RegWrite and (MEM_WB.rd != 0) and not (EX_MEM.RegWrite and (EX_MEM.rd != 0)
            and (EX_MEM.rd == ID_EX.rs)) and (MEM_WB.rd == ID_EX.rs):
            # Forward to rs
            ID_EX = MEM_WB

        if MEM_WB.RegWrite and (MEM_WB.Rrd != 0) and not (EX_MEM.RegWrite and (EX_MEM.rd != 0)
            and (EX_MEM.rd == ID_EX.rt)) and (MEM_WB.rd == ID_EX.rt):
            # Forward to rt
            ID_EX = MEM_WB

        return not (ID_EX.RegisterRs_value or ID_EX.RegisterRt_value)

    def NOP(self):
        self.ID_EX = None
