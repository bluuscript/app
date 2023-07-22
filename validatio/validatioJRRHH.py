import sys
sys.path.append(".")

from dto.dtoJRRHH import dtoJRRHH
from validatio.validatioRRHH import *
from validatio.validatioPersonal import menuMiRegistro

def filtrarRegistros():
    filter1 = input("\n¿Desea filtrar por Género? (s/n)\n:")
    if filter1 == "s":
        genFiltro = input("Ingrese Género a filtrar\n:")
    else:
        genFiltro = ""
        
    filter2 = input("\n¿Desea filtrar por Cárgo? (s/n)\n:")
    if filter2 == "s":
        carFiltro = input("Ingrese Cargo a filtrar\n:")
    else:
        carFiltro = ""
        
    filter3 = input("\n¿Desea filtrar por Área? (s/n)\n:")
    if filter3 == "s":
        areaFiltro = input("Ingrese Área a filtrar\n:")
    else:
        areaFiltro = ""
        
    filter4 = input("\n¿Desea filtrar por Departamento? (s/n)\n:")
    if filter4 == "s":
        depFiltro = input("Ingrese Departamento a filtrar\n:")
    else:
        depFiltro = ""
        
    respuesta = dtoJRRHH().registrosNominaFiltro(
        personalGenero=genFiltro, cargoNombre=carFiltro,
        areaNombre=areaFiltro, departamentoNombre=depFiltro)
    print("""\n
            Registros Nomina Personal - Resumen
            
          """)
    if respuesta is not None:
        for registro in respuesta:
            print(registro)

        
def menuJRRHH(usuarioPersonalRut):
    salir = "n"
    while salir == "n":
        print("""
                1. Mi Registro
                
                    Administrar Nomina
                    
                2. Agregar Nuevo Registro
                3. Listar Registros
                4. Modificar Registro
                5. Eliminar Registro
                
                6. Filtrar Registros
                                
                7. Salir
              """)
        opcion = int(input("> "))
        if opcion == 1:
            menuMiRegistro(personalRut=usuarioPersonalRut)
        elif opcion == 2:
            agregarPersonal()
        elif opcion == 3:
            registrosNomina()
        elif opcion == 4:
            modificarRegistro()
        elif opcion == 5:
            eliminarRegistro()
        elif opcion == 6:
            filtrarRegistros()
        elif opcion == 7:
            break
        else:
            pass
        volver = input("Desea volver al Menu? [s/n] > ")
