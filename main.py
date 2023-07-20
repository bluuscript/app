import sys
sys.path.append(".")
from validatio.validatioUsuarios import autenticarUsuario

from validatio.validatioPersonal import menuMiRegistro
from validatio.validatioRRHH import menuRRHH
#from validatio.validatioJRRHH import menuJRRHH

intentos = 0

while intentos < 3:
    resultado = autenticarUsuario()
    if resultado is not None:
        print(f"Bienvenido(a) Sr(a). {resultado.usuarioNombre}")
        if resultado.usuarioTipoPersonal == "COMUN":
            menuMiRegistro(resultado.usuarioPersonalRut)
        elif resultado.usuarioTipoPersonal == "RRHH":
            menuRRHH(usuarioPersonalRut=resultado.usuarioPersonalRut)
        elif resultado.usuarioTipoPersonal == "JRRHH":
            #menuJRRHH()
            pass
        break
    else:
        print("Usuario y/o contraseña incorrectos")
        intentos += 1
