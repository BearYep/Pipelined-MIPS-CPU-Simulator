class Data_Hazard:
    def data_hazard_detection(IF_ID, reg_file):
        if IF_ID.opcode == "lw" or IF_ID.opcode == "sw":
            if IF_ID.rt == reg_file[IF_ID.rs] or IF_ID.rt == reg_file[IF_ID.rt]:
                return True
        elif IF_ID.opcode == "add" or IF_ID.opcode == "sub":
            if IF_ID.rd == reg_file[IF_ID.rs] or IF_ID.rd == reg_file[IF_ID.rt]:
                return True
        elif IF_ID.opcode == "beq":
            if IF_ID.rs == reg_file[IF_ID.rs] or IF_ID.rt == reg_file[IF_ID.rt]:
                return True
        return False
    
    def forwarding(ID_EX, EX_MEM, MEM_WB):
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
