class persona:
    def __init__(self, PER_ID, PER_UUID, PER_CONTRASEÑA, PER_NUMERO_DOCUMENTO, PER_PRIMER_NOMBRE, PER_SEGUNDO_NOMBRE, PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO,):
        self.CAR_ID                   = PER_ID
        self.CAR_UUID                 = PER_UUID
        self.PER_CONTRASENA           = PER_CONTRASEÑA
        self.PER_NUMERO_DOCUMENTO     = PER_NUMERO_DOCUMENTO
        self.PER_PRIMER_NOMBRE        = PER_PRIMER_NOMBRE
        self.PER_SEGUNDO_NOMBRE       = PER_SEGUNDO_NOMBRE
        self.PER_PRIMER_APELLIDO      = PER_PRIMER_APELLIDO
        self.PER_SEGUNDO_APELLIDO     = PER_SEGUNDO_APELLIDO


    def to_dict(self):
        return{
            'PER_ID'         : self.PER_ID,
            'PER_UUID'       : self.PER_UUID, 
            'PER_CONTRASENA' : self.PER_CONTRASENA,
            'PER_NUMERO_DOCUMENTO'      : self.PER_NUMERO_DOCUMENTO, 
            'PER_PRIMER_NOMBRE'         : self.PER_PRIMER_NOMBRE, 
            'PER_SEGUNDO_NOMBRE'        : self.PER_SEGUNDO_NOMBRE, 
            'PER_PRIMER_APELLIDO'       : self.PER_PRIMER_APELLIDO,
            'PER_SEGUNDO_APELLIDO'      : self.PER_SEGUNDO_APELLIDO
        }