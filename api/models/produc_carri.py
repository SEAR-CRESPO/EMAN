class produc_carri:
    def __init__(self, PROC_ID, PROC_UUID, PROC_CANTIDAD, PROC_PRO_ID, PROC_COMC_ID):
        self.PROC_ID       = PROC_ID
        self.PROC_UUID     = PROC_UUID
        self.PROC_CANTIDAD = PROC_CANTIDAD
        self.PROC_PRO_ID   = PROC_PRO_ID
        self.PROC_COMC_ID  = PROC_COMC_ID 



    def to_dict(self):
        return{
            'PROC_ID'       : self.PROC_ID,
            'PROC_UUID'     : self.PROC_UUID,
            'PROC_CANTIDAD' :self.PROC_CANTIDAD,
            'PROC_PRO_ID'   : self.PROC_PRO_ID,
            'PROC_COMC_ID'  : self.PROC_COMC_ID
        }
  