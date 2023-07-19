import sys
sys.path.append(".")
from conn.conn import ConectarBD
from modelo.usuario import *

class daoUsuario:
    def __init__(self):
        try:
            self.conn= ConectarBD("localhost", "root", "", "testnomina")
        except Exception as ex:
            print(ex)
        self.cursor = self.conn.getCursor()

    def getConn(self):
        return self.conn

    def autenticarUsuario(self, usuarioCorreo, usuarioContraseña):
        sql="""SELECT usuarioCorreo, usuarioNombre, usuarioTipoPersonal, 
        usuarioPersonalRut FROM `usuario` WHERE `usuarioCorreo`=%s AND `usuarioContraseña`=%s"""
        try:
            self.cursor.execute( sql, (usuarioCorreo, usuarioContraseña,) )
            usuario = self.cursor.fetchone()
        except Exception as error:
            print(error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
        return usuario
    
    def getUsuario(self, Usuario):
        sql_buscarUsuario = "SELECT `usuarioCorreo`, `usuarioNombre`, `usuarioContraseña`, \
            `usuarioTipoPersonal`, `usuarioPersonalRut` FROM `usuario` WHERE \
            `usuarioCorreo`=%s"
        try:
            self.cursor.execute( sql_buscarUsuario, (Usuario.usuarioCorreo,) )
            usuario = self.cursor.fetchone()
        except Exception as error:
            print(error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
        return usuario
        
    def addUsuario(self, Usuario):
        sql_insertarUsuario = "INSERT INTO `usuario` (`usuarioNombre`, `usuarioCorreo`, \
            `usuarioContraseña`, `usuarioTipoPersonal`, `usuarioPersonalRut`) \
            VALUES (%s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql_insertarUsuario, (Usuario.usuarioNombre, Usuario.usuarioCorreo, \
                Usuario.usuarioContraseña, Usuario.usuarioTipoPersonal, Usuario.usuarioPersonalRut,))
            self.conn.getConn().commit()
        except Exception as error:
            print(f"Insertar Usuario {Usuario.usuarioCorreo} error: ", error)
        
"""user = Usuario(usuarioNombre="Tomás", 
               usuarioCorreo="tomymilla22@gmail.com",
            usuarioContraseña="123",
            usuarioTipoPersonal="RRHH",
            usuarioPersonalRut="20916538-4")
daoUser = daoUsuario()
print(daoUser.authUsuario(Usuario=user))"""

# PENDIENTE = CIFRAR Y CONSULTAR CONTRASEÑA PARA: DESCIFRAR / CHECK
user1 = Usuario(usuarioNombre="Tomás1", 
               usuarioCorreo="bluu@yury.cl",
            usuarioContraseña="321",
            usuarioTipoPersonal="JRRHH",
            usuarioPersonalRut="1-1")

daoUser = daoUsuario()
#print(daoUser.getUsuario(Usuario=Usuario(usuarioCorreo="adansanmartin@gmail.com")))
