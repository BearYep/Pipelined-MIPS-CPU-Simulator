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
        if EX_MEM and EX_MEM.opcode in ["add", "sub", "lw", "sw"]:
            if ID_EX.RegisterRs == EX_MEM.RegisterRd:
                ID_EX.RegisterRs_value = EX_MEM.ALU_result
            if ID_EX.RegisterRt == EX_MEM.RegisterRd:
                ID_EX.RegisterRt_value = EX_MEM.ALU_result

        # MEM hazard
        elif MEM_WB and MEM_WB.opcode in ["add", "sub", "lw", "sw"]:
            if  ID_EX.RegisterRs == MEM_WB.RegisterRd:
                ID_EX.RegisterRs_value = MEM_WB.MEM_result
            if ID_EX.RegisterRt == MEM_WB.RegisterRd:
                ID_EX.RegisterRt_value = MEM_WB.MEM_result
