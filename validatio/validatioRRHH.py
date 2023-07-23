import sys
sys.path.append(".")

from dto.dtoRRHH import dtoRRHH
from validatio.validatioPersonal import menuMiRegistro
from validatio.validatioPersonal import miRegistro

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
        cargoFechaIngreso = input("Fecha de Ingreso YYYY/MM/DD: ")
        if cargoFechaIngreso == date:
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
        contactoRut = input("RUT: ")
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
            contactoRut=contactoRut, contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros
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
    if personalRut == "":
        print("Dato vacío. Inténtelo de nuevo")
    resultado = dtoRRHH().buscarRegistro(personalRut=personalRut)
    
    if resultado is True:
        print(f"""              
                    ********** Registro de {personalRut} **********
                        
              """)
        miRegistro(personalRut=personalRut)
        modificar_datos_personales = input("\nQuiere modificar algún Dato Personal? [s/n] > ").lower()
        if modificar_datos_personales.strip() == "s":
            print("""
                    Nuevos Datos Personales
                """)
            personalNuevoNombre = input("Nombre: ")
            personalNuevaDireccion = input("Direccion: ")
            personalNuevoGenero = input("Género: ")
            resultado_modPersonal = dtoRRHH().modificarPersonal(
                personalRut=personalRut, personalNombre=personalNuevoNombre,
                personalGenero=personalNuevoGenero, personalDireccion=personalNuevaDireccion
            )
        pregunta = input("\n¿Desea editar Datos Laborales? [s/n] > ").lower()
        if pregunta.strip() == "s":
            print("""
                Nuevos Datos Laborales
              """)
            cargoNombre = input("Cargo: ")
            cargoFechaIngreso = input("Fecha de Ingreso (formato YYYY/MM/DD): ")
            departamentoNombre = input("Departamento: ")
            areaNombre = input("Area: ")
            resp_lab = dtoRRHH().modificarDatosLaborales(personalRut = personalRut, cargoNombre = cargoNombre, cargoFechaIngreso = cargoFechaIngreso, areaNombre = areaNombre, departamentoNombre = departamentoNombre)
            
        mod_or_add_contacto = input("\nQuiere Agregar o Eliminar algún Contacto? [s/n] > ").lower()
        if mod_or_add_contacto.strip() == "s":
            print("""
                    1. Añadir Contacto
                    2. Eliminar Contacto
                    3. Salir / Cancelar
                """)
            opcion = int(input("> "))
            if opcion == 1:
                print("""
                    Datos Nuevo Contacto de Emergencia
                """)
                contactoRut = input("RUT: ")
                contactoNombre = input("Nombre: ")
                contactoRelacionPersonal = input("Relacion con Personal: ")
                telefonoContactoNumeros = []
                agregar_telefonoContacto = "s"
                while agregar_telefonoContacto == "s":
                    telefonoContacto = input("Número de Telefono: +569 ")
                    telefonoContactoNumeros.append(telefonoContacto)
                    agregar_telefonoContacto = input("Desea agregar otro telefono? [s/n]").lower()
                resultado_agregarContacto = dtoRRHH().agregarContacto(
                    personalRut=personalRut, contactoRut=contactoRut, contactoNombre=contactoNombre,
                    contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros
                )
            elif opcion == 2:
                contactoRut = input("Ingrese RUT Contacto a Eliminar: ")
                resultado_eliminar_contacto = dtoRRHH().eliminarContacto(contactoRut=contactoRut)
            elif opcion == 3:
                pass
            else:
                pass
            
        mod_or_add_carga = input("\nQuiere Agregar o Eliminar alguna Carga? [s/n] > ").lower()
        if mod_or_add_carga.strip() == "s":
            print("""
                    1. Añadir Carga
                    2. Eliminar Carga
                    3. Salir / Cancelar
                """)
            opcion = int(input("> "))
            if opcion == 1:
                print("""
                    Datos Nueva Carga Familiar
                    
                """)
                cargaRut = input("RUT: ")
                cargaNombre = input("Nombre: ")
                cargaGenero = input("Género: ")
                cargaParentesco = input("Parentesco: ")
                
                resultado_agregarCarga = dtoRRHH().agregarCarga(
                    personalRut=personalRut, cargaRut=cargaRut,
                    cargaNombre=cargaNombre, cargaGenero=cargaGenero,
                    cargaParentesco=cargaParentesco
                )
                
            elif opcion == 2:
                print("""
                    Eliminar Carga Familiar
                    
                """)
                cargaRut = input("Ingrese RUT Carga: ")
                resultado_eliminarCarga =  dtoRRHH().eliminarCarga(cargaRut=cargaRut)
            elif opcion == 3:
                pass
            else:
                pass 
        
def eliminarRegistro():
    print("""
            Eliminar Registro Personal
            
          """)
    personalRut = input("RUT personal a Eliminar: ")
    
    resultado = dtoRRHH().buscarRegistro(personalRut=personalRut)
    
    if resultado is not None:
        return dtoRRHH().eliminarPersonal(personalRut=personalRut)
    else:
        print(f"No Existe Registro con RUT: {personalRut}")

def menuRRHH(usuarioPersonalRut):
    salir = "n"
    while salir == "n":
        print("""
                1. Mi Registro
                    
                   📮 Administrar Nomina 🗃️
            
                2. Agregar Nuevo Registro   
                3. Listar Registros         
                4. Modificar Registro       
                5. Eliminar Registro        
                
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
        salir = input("Desea salir del Menu? [s/n] > ")