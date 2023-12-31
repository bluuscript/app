import sys
sys.path.append(".")
from modelo.usuario import Usuario
from dao.daoUsuario import daoUsuario

class UsuarioDTO:
    
    def autenticarUsuario(self, usuarioCorreo, usuarioContraseña):
        daousuario = daoUsuario()
        resultado = daousuario.autenticarUsuario(usuarioCorreo = usuarioCorreo, usuarioContraseña = usuarioContraseña)
        if resultado is not None:
            return Usuario(
                    usuarioCorreo=resultado[0],
                    usuarioNombre=resultado[1],
                    usuarioTipoPersonal=resultado[2],
                    usuarioPersonalRut=resultado[3])
        else: None
    
    def insertarUsuario(self, usuarioNombre, usuarioCorreo, usuarioContraseña, usuarioTipoPersonal, usuarioPersonalRut):
        daousuario = daoUsuario()
        resultado = daousuario.addUsuario(Usuario(usuarioNombre = usuarioNombre, usuarioCorreo = usuarioCorreo, usuarioContraseña = usuarioContraseña, usuarioTipoPersonal = usuarioTipoPersonal, usuarioPersonalRut = usuarioPersonalRut))
        return resultado if resultado else None
    
    def buscarUsuario(self, usuarioCorreo):
        daouser = daoUsuario()
        resultado = daouser.getUsuario(Usuario=Usuario(usuarioCorreo=usuarioCorreo))
        return Usuario(usuarioCorreo=resultado[0], usuarioNombre=resultado[1],
                     usuarioTipoPersonal=resultado[3], usuarioPersonalRut=resultado[4]) if resultado is not None else None
