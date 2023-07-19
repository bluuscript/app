import sys
sys.path.append(".")

from dto.dtoRRHH import dtoRRHH

def agregarPersonal():
    print("""
            Agregar Nuevo Personal a Nomina
          """)
    personalRut = input("RUT: ")
    
    resultado = dtoRRHH().buscarRegistro(personalRut)
    
    if resultado is None:
        print("""
                Datos Personales
              """)
        personalNombre = input("Nombre: ")
        personalGenero = input("Género: ")
        personalDireccion = input("Dirección: ")
        telefonosPersonalNumeros = []
        agregar_telefonoPersonal = "s"
        while agregar_telefonoPersonal == "s":
            telefonoPersonal = input("Número de Telefono: +569")
            telefonosPersonalNumeros.append(telefonoPersonal)
            agregar_telefonoPersonal = input("Desea agregar otro telefono? [s/n]")
        print("""
                Datos Laborales
              """)
        cargoNombre = input("Cargo: ")
        cargoFechaIngreso = input("Fecha de Ingreso: ")
        departamentoNombre = input("Departamento: ")
        areaNombre = input("Area: ")
        print("""
                Datos Contactos de Emergencia
              """)
        contactoNombre = input("Nombre: ")
        contactoRelacionPersonal = input("Relacion con Personal: ")
        telefonoContactoNumeros = []
        agregar_telefonoContacto = "s"
        while agregar_telefonoContacto == "s":
            telefonoContacto = input("Número de Telefono: +569")
            telefonoContactoNumeros.append(telefonoContacto)
            agregar_telefonoContacto = input("Desea agregar otro telefono? [s/n]")
        print("""
                Datos Cargas Familiares
              """)
        cargaRut = input("Carga RUT: ")
        cargaNombre = input("Nombre: ")
        cargaGenero = input("Género: ")
        cargaParentesco = input("Parentesco: ")
    else: 
        print(f"Registro RUT: {personalRut} ya Existe")
    return

def registrosNomina():
    
    return dtoRRHH().registrosNomina()


agregarPersonal()
