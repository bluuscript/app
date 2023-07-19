import sys
sys.path.append(".")
from validatio.validatioUsuarios import autenticarUsuario

intentos = 0

while intentos <= 3:
    resultado = autenticarUsuario()
    if resultado is not None:
        print(f"Bienvenido(a) Sr(a). {resultado.usuarioNombre}")
        # Inicializar Menu
        break
    else:
        print("Usuario y/o contraseña incorrectos")
        intentos += 1
