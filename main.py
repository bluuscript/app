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
        # Tipo de Personal en La Empresa Dividio en 3 Grupos
        tipoPersonal = resultado.usuarioTipoPersonal.upper()
        print(f"Bienvenido(a) Sr(a). {resultado.usuarioNombre}")
        if tipoPersonal== "COMUN":
            menuMiRegistro(personalRut=resultado.usuarioPersonalRut)
        elif tipoPersonal == "RRHH":
            menuRRHH(usuarioPersonalRut=resultado.usuarioPersonalRut)
        elif tipoPersonal == "JRRHH":
            #menuJRRHH()
            pass
        break
    else:
        print("Usuario y/o contraseña incorrectos")
        intentos += 1
