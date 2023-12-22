class Data_Hazard:

    def detection(self, ID_EX, EX_MEM, MEM_WB):
        if not self.forwarding(ID_EX, EX_MEM, MEM_WB):
            self.NOP()

    def forwarding(self, ID_EX, EX_MEM, MEM_WB):
        # EX hazard
        if EX_MEM.RegWrite and (EX_MEM.RegisterRd != 0) and (EX_MEM.RegisterRd == ID_EX.RegisterRs):
            # Forward to rs
            ID_EX.RegisterRs_value = EX_MEM.ALU_result

        if EX_MEM.RegWrite and (EX_MEM.RegisterRd != 0) and (EX_MEM.RegisterRd == ID_EX.RegisterRt):
            # Forward to rt
            ID_EX.RegisterRt_value = EX_MEM.ALU_result

        # MEM hazard
        if MEM_WB.RegWrite and (MEM_WB.RegisterRd != 0) and not (EX_MEM.RegWrite and (EX_MEM.RegisterRd != 0)
            and (EX_MEM.RegisterRd == ID_EX.RegisterRs)) and (MEM_WB.RegisterRd == ID_EX.RegisterRs):
            # Forward to rs
            ID_EX.RegisterRs_value = MEM_WB.MEM_result

        if MEM_WB.RegWrite and (MEM_WB.RegisterRd != 0) and not (EX_MEM.RegWrite and (EX_MEM.RegisterRd != 0)
            and (EX_MEM.RegisterRd == ID_EX.RegisterRt)) and (MEM_WB.RegisterRd == ID_EX.RegisterRt):
            # Forward to rt
            ID_EX.RegisterRt_value = MEM_WB.MEM_result

        return not (ID_EX.RegisterRs_value or ID_EX.RegisterRt_value)

    def NOP(self):
        pass
