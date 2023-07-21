import sys
sys.path.append(".")

from dto.dtoRRHH import dtoRRHH
from validatio.validatioPersonal import menuMiRegistro

from datetime import date

def agregarPersonal():
    print("""
            Agregar Nuevo Personal a Nomina
          """)
    personalRut = input("RUT: ")
    
    resultado = dtoRRHH().buscarRegistro(personalRut=personalRut)
    
    if resultado is None:
        print("""
                Datos Personales
              """)
        personalNombre = input("Nombre: ")
        personalGenero = input("Género: ")
        personalDireccion = input("Dirección: ")
        telefonoPersonalNumeros = []
        agregar_telefonoPersonal = "s"
        while agregar_telefonoPersonal == "s":
            telefonoPersonal = input("Número de Telefono: +569 ")
            telefonoPersonalNumeros.append(telefonoPersonal)
            agregar_telefonoPersonal = input("Desea agregar otro telefono? [s/n]")
        print("""
                Datos Laborales
              """)
        cargoNombre = input("Cargo: ")
        #cargoFechaIngreso = input("Fecha de Ingreso: ")
        cargoFechaIngreso = date.today()
        departamentoNombre = input("Departamento: ")
        areaNombre = input("Area: ")
        
        print("""
                Datos Cargas Familiares
              """)
        cargaRut = input("Carga RUT: ")
        cargaNombre = input("Nombre: ")
        cargaGenero = input("Género: ")
        cargaParentesco = input("Parentesco: ")
        
        print("""
                Datos Contactos de Emergencia
              """)
        contactoNombre = input("Nombre: ")
        contactoRelacionPersonal = input("Relacion con Personal: ")
        telefonoContactoNumeros = []
        agregar_telefonoContacto = "s"
        while agregar_telefonoContacto == "s":
            telefonoContacto = input("Número de Telefono: +569 ")
            telefonoContactoNumeros.append(telefonoContacto)
            agregar_telefonoContacto = input("Desea agregar otro telefono? [s/n]")
        
        insertarRegistro = dtoRRHH().agregarPersonalNomina(
            # Personales
            personalRut=personalRut, personalNombre=personalNombre, personalGenero=personalGenero, personalDireccion=personalDireccion,
            # Telefono Personal
            telefonoPersonalNumeros=telefonoPersonalNumeros,
            # Cargo
            cargoNombre=cargoNombre, cargoFechaIngreso=cargoFechaIngreso,
            # Departamento y Area
            departamentoNombre=departamentoNombre, areaNombre=areaNombre,
            # Carga
            cargaRut=cargaRut, cargaNombre=cargaNombre, cargaGenero=cargaGenero, cargaParentesco=cargaParentesco,
            # Contacto
            contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros
        )
        return insertarRegistro
    else: 
        print(f"Registro RUT: {personalRut} ya Existe")

def registrosNomina():
    print("""
            Registros Nomina Personal - Resumen
            
          """)
    registros = dtoRRHH().registrosNomina()
    if registros is not None:
        for registro in registros:
            print(registro)
    else:
        print("No Existen Registros")
        

def modificarRegistro():
    print("""
            Modificar Registro Personal
            
          """)
    personalRut = input("RUT Personal a Modificar: ")
    
    resultado = dtoRRHH().buscarRegistro(personalRut=personalRut)
    
    if resultado is not None:
        print("Registro: ", resultado)
        print("""
                Datos Personales
              """)
        personalNombre = input("Nombre: ")
        personalGenero = input("Género: ")
        personalDireccion = input("Dirección: ")
        telefonosPersonalNumeros = []
        agregar_telefonoPersonal = "s"
        while agregar_telefonoPersonal == "s":
            telefonoPersonal = input("Número de Telefono: +569 ")
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

def eliminarRegistro():
    print("""
            Eliminar Registro Personal
            
          """)
    personalRut = input("RUT personal a Eliminar: ")
    
    resultado = dtoRRHH().buscarRegistro(personalRut=personalRut)
    
    if resultado is not None:
        return dtoRRHH().eliminarPersonal(personalRut=personalRut)

def menuRRHH(usuarioPersonalRut):
    volver = "s"
    while volver == "s":
        print("""
                1. Mi Registro
                    
                    Administrar Nomina
                    
                2. Agregar Nuevo Registro   ✅
                3. Listar Registros         ✅
                4. Modificar Registro       ❌
                5. Eliminar Registro        ✅
                
                6. Salir
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
            break
        else:
            pass
        volver = input("Desea volver al Menu? [s/n] > ")