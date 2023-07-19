
class Usuario:
    def __init__(self, usuarioCorreo="", usuarioNombre="", usuarioContraseña="", usuarioTipoPersonal="", usuarioPersonalRut=""):
        self.usuarioCorreo = usuarioCorreo
        self.usuarioNombre = usuarioNombre
        self.usuarioContraseña = usuarioContraseña
        self.usuarioTipoPersonal = usuarioTipoPersonal
        self.usuarioPersonalRut = usuarioPersonalRut
            
    def getUsuarioCorreo(self):
        return self.usuarioCorreo
    
    def __str__(self):
        return f"{self.usuarioCorreo} - {self.usuarioNombre} - {self.usuarioTipoPersonal} - {self.usuarioPersonalRut}"

#user = Usuario("t@gmail.com", "Tomas", "12345678", "JRRHH", "1-1")
