import sys
sys.path.append(".")
from utils.encoder import Encoder
from dto.dtoUsuario import UsuarioDTO

# Para todo el Personal que Quiera Ingresar
def autenticarUsuario():
    print("""
                Login
           Nomina Personal
          El Correo de Yury
        """)
    usuarioCorreo = input("Correo > ")
    usuarioContraseña = input("Contraseña > ")
    respuesta = UsuarioDTO().autenticarUsuario(usuarioCorreo,Encoder().encode(usuarioContraseña))
    return respuesta if respuesta is not None else None

# 💫 SOLO RRHH y JRRHH       
def insertarUsuario():
    print("\n\tInsertar Nuevo Usuario\n")
    usuarioCorreo = input("Correo > ")
    if len(usuarioCorreo) == 0:
        salida = input("\nDesea Volver al Menú Principal [s/n] > ").lower()
        if salida == "n":
            insertarUsuario()
        else:
            return
    resultado = UsuarioDTO().buscarUsuario(usuarioCorreo)
    if not resultado:
        # Datos Usuario
        usuarioNombre = input("Nombre > ")
        usuarioClave = input("Contraseña* > ")
        usuarioTipoPersonal = input("Tipo de Personal (COMUN - RRHH - JRRHH) > ")
        usuarioPersonalRut = input("RUT* > ")
        if usuarioClave == '' or usuarioPersonalRut == '':
            print("Contraseña y RUT Usuario REQUERIDOS")
            # Volver a Intentarlo 🚘 AUTO
            insertarUsuario()
        else:
            UsuarioDTO().insertarUsuario(usuarioNombre, usuarioCorreo, Encoder().encode(usuarioClave), usuarioTipoPersonal, usuarioPersonalRut)
    else:
        print(f"Usuario Correo: {usuarioCorreo} ya registrado")
        # Volver a Intentarlo 🚘 AUTO
        insertarUsuario()

#insertarUsuario()