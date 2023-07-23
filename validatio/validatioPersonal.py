import sys
sys.path.append(".")
from dto.dtoPersonal import dtoPersonal

def miRegistro(personalRut):

    resultado = dtoPersonal().existeRegistro(personalRut=personalRut)
    
    if resultado is not None:
        mi_registro = dtoPersonal().miRegistro(personalRut=personalRut)
        print(f"""
                    Datos Personales
                    
                    {mi_registro[0]}
                        
                    Telefonos:""")
        for telefono in mi_registro[2]:
            print(f""" 
                        {telefono}""")
        print(f"""
                    Datos Laborales
                
                {mi_registro[1]['Cargo']}
                
                {mi_registro[1]['Departamento']}
                
                {mi_registro[1]['Area']}""")
        
        print("""
                        Cargas Familiares:""")
        for carga in mi_registro[3]:
            print(f""" 
                            {carga}""")
        
        print("""
                        Contactos de Emergencia:""")
        for contacto in mi_registro[4]:
            print(f""" 
                            {contacto}
                            
                                Telefonos Contacto:""")
            for telefonosContacto in mi_registro[5]:
                if contacto.contactoID == telefonosContacto['contactoID']:
                    for telefonoContacto in telefonosContacto['telefonosContacto']:
                        print(f""" 
                                        · {telefonoContacto[0]}""")
                        
    else:
        print(f"No existe registro RUT: {personalRut}")
        
def modificarMiRegistro(personalRut):
    print(f"""
                        Modificar Mi Registro
            ( Dejar en blanco los atributos que no quiera modificar )
          """)
    # Registro Usuario Para que Elija que datos modificar
    miRegistro(personalRut=personalRut)

    modificar_datos_personales = input("\nQuiere modificar algún dato personal? [s/n] > ").lower()
    if modificar_datos_personales.strip() == "s":
        # Modificar Datos Personales
        personalNuevoNombre = input("Nombre: ")
        personalNuevaDireccion = input("Direccion: ")
        personalNuevoGenero = input("Género: ")
        modificar_personal = dtoPersonal().modificarMiRegistro(
                personalRut=personalRut, personalNombre=personalNuevoNombre,
                personalGenero=personalNuevoGenero, personalDireccion=personalNuevaDireccion
            )
    mod_or_add_contacto = input("\nQuiere Agregar o Eliminar algún Contacto de Emergencia? [s/n] > ").lower()
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
            while agregar_telefonoContacto.strip() == "s":
                telefonoContacto = input("Número de Telefono: +569 ")
                telefonoContactoNumeros.append(telefonoContacto)
                agregar_telefonoContacto = input("\nDesea agregar otro telefono? [s/n]").lower()
            resultado_agregarContacto = dtoPersonal().agregarContacto(
                personalRut=personalRut, contactoRut=contactoRut, contactoNombre=contactoNombre,
                contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros
            )
            #return resultado_agregarContacto if resultado_agregarContacto is not None or resultado_agregarContacto is not UnboundLocalError else None
        elif opcion == 2:
            contactoRut = input("Ingrese RUT Contacto a Eliminar: ")
            eliminar_contacto = dtoPersonal().eliminarContacto(contactoRut=contactoRut)
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
            
            resultado_agregarCarga = dtoPersonal().agregarCarga(
                personalRut=personalRut, cargaRut=cargaRut,
                cargaNombre=cargaNombre, cargaGenero=cargaGenero,
                cargaParentesco=cargaParentesco
            )
            
        elif opcion == 2:
            print("""
                Eliminar Carga Familiar
                
              """)
            cargaRut = input("Ingrese RUT Carga: ")
            eliminar_carga = dtoPersonal().eliminarCarga(cargaRut=cargaRut)
        elif opcion == 3:
            pass
        else:
            pass

def menuMiRegistro(personalRut):
    salir = "n"
    while salir == "n":
        print(f"""
                1. Ver Registro            
                2. Modificar Mi Registro    
                3. Salir
        """)
        opcion = int(input("> "))
        
        if opcion == 1:
            miRegistro(personalRut=personalRut)
        elif opcion == 2:
            modificarMiRegistro(personalRut=personalRut)
        elif opcion == 3:
            break
        salir = input("\nDesea Salir de Mi Registro? [s/n] > ")
        