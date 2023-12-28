
def detection(ID_EX, EX_MEM, MEM_WB):
    if not forwarding(ID_EX, EX_MEM, MEM_WB):
        NOP()

def forwarding(ID_EX, EX_MEM, MEM_WB):
    if EX_MEM and MEM_WB:
    # EX hazard
        if EX_MEM.RegWrite and (EX_MEM.rd != 0) and (EX_MEM.rd == ID_EX.rs):
            return 'EX_hazard_rs'

        if EX_MEM.RegWrite and (EX_MEM.rd != 0) and (EX_MEM.rs == ID_EX.rt):
            return 'EX_hazard_rt'

        # MEM hazard
        if MEM_WB.RegWrite and (MEM_WB.rd != 0) and not (EX_MEM.RegWrite and (EX_MEM.rd != 0)
            and (EX_MEM.rd == ID_EX.rs)) and (MEM_WB.rd == ID_EX.rs):
            # Forward to rs
            return 'MEM_hazard_rs'

        if MEM_WB.RegWrite and (MEM_WB.rd != 0) and not (EX_MEM.RegWrite and (EX_MEM.rd != 0)
            and (EX_MEM.rd == ID_EX.rt)) and (MEM_WB.rd == ID_EX.rt):
            # Forward to rt
            return 'MEM_hazard_rt'

    return None

def NOP():
    ID_EX = None
