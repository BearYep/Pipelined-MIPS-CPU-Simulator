
def detection(ID_EX, EX_MEM, MEM_WB):
    if not forwarding(ID_EX, EX_MEM, MEM_WB):
        NOP()

def detect_Hazard(ID_EX, EX_MEM, MEM_WB, forwardingUnit):
    if EX_MEM and MEM_WB:
        # EX hazard
        if EX_MEM.RegWrite and (EX_MEM.rd != 0) and (EX_MEM.rd == ID_EX.rs):
            forwardingUnit.ForwardA = 0b10

        if EX_MEM.RegWrite and (EX_MEM.rd != 0) and (EX_MEM.rd == ID_EX.rt):
            forwardingUnit.ForwardB = 0b10

        # MEM hazard
        if MEM_WB.RegWrite and (MEM_WB.rd != 0) and not (EX_MEM.RegWrite and (EX_MEM.rd != 0)
            and (EX_MEM.rd == ID_EX.rs)) and (MEM_WB.rd == ID_EX.rs):
            # Forward to rs
            forwardingUnit.ForwardA = 0b01

        if MEM_WB.RegWrite and (MEM_WB.rd != 0) and not (EX_MEM.RegWrite and (EX_MEM.rd != 0)
            and (EX_MEM.rd == ID_EX.rt)) and (MEM_WB.rd == ID_EX.rt):
            # Forward to rt
            forwardingUnit.ForwardB = 0b01

def load_use_hazard(IF_ID, ID_EX):
    if IF_ID and ID_EX:
        if ID_EX.MemRead and ((ID_EX.rt == IF_ID.rs) or (ID_EX.rt == IF_ID.rt)):
            #Stall and insert bubble
            return True
            
    return False

def branch_hazard(IF_ID, ID_EX, EX_MEM, MEM_WB, forwardingUnit):
    condition_result = 0b00
    if(IF_ID and IF_ID.opcode == 'beq'):
        if (MEM_WB and IF_ID) or (EX_MEM and IF_ID):
            #2nd or 3rd

            if (MEM_WB and IF_ID):
                if(MEM_WB.RegWrite and (MEM_WB.rd) != 0):
                    if(MEM_WB.rd == IF_ID.rs):
                        forwardingUnit.ForwardA = 0b01
                    if(MEM_WB.rd == IF_ID.rt):
                        forwardingUnit.ForwardB = 0b01
                    condition_result = 0b01
            
            if(EX_MEM and IF_ID):
                if(EX_MEM.RegWrite and (EX_MEM.rd) != 0):
                    if(EX_MEM.rd == IF_ID.rs):
                        forwardingUnit.ForwardA = 0b10
                    if(EX_MEM.rd == IF_ID.rt):
                        forwardingUnit.ForwardB = 0b10
                    condition_result = 0b01

            if MEM_WB and IF_ID and EX_MEM:
                if(EX_MEM.RegWrite and (EX_MEM.rd) != 0):
                    if(EX_MEM.rd == IF_ID.rs):
                        forwardingUnit.ForwardA = 0b10
                    if(EX_MEM.rd == IF_ID.rt):
                        forwardingUnit.ForwardB = 0b10
                    condition_result = 0b01

                if(MEM_WB.RegWrite and (MEM_WB.rd) != 0) and not(EX_MEM.RegWrite and (EX_MEM.rd) != 0):
                    if(MEM_WB.rd == IF_ID.rs):
                        forwardingUnit.ForwardA = 0b01
                    if(MEM_WB.rd == IF_ID.rt):
                        forwardingUnit.ForwardB = 0b01
                    condition_result = 0b01

        
        if EX_MEM and ID_EX and IF_ID:
                if(ID_EX.RegWrite and (ID_EX.rd) != 0):
                    if(ID_EX.rd == IF_ID.rs):
                        forwardingUnit.ForwardA = 0b10
                    if(ID_EX.rd == IF_ID.rt):
                        forwardingUnit.ForwardB = 0b10
                    condition_result = 0b10

                if(EX_MEM.MemRead):
                    if(EX_MEM.rt == IF_ID.rs):
                        forwardingUnit.ForwardA = 0b01
                    if(EX_MEM.rt == IF_ID.rt):
                        forwardingUnit.ForwardB = 0b01
                    condition_result = 0b10

        
        if ID_EX and IF_ID:
            if (ID_EX.MemRead):
                if(ID_EX.rt == IF_ID.rs):
                    forwardingUnit.ForwardA = 0b10
                    condition_result = 0b11 

                if(ID_EX.rt == IF_ID.rt):
                    forwardingUnit.ForwardB = 0b10
                    condition_result = 0b11
    return condition_result
            

def NOP():
    return None
