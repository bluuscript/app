import sys
sys.path.append(".")
from dto.dtoPersonal import dtoPersonal

def miRegistro(personalRut):

    resultado = dtoPersonal().existeRegistro(personalRut=personalRut)
    
    if resultado is True:
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
                
                {mi_registro[1]['Area']}

            """)
        
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
        for telefonoContacto in mi_registro[5]:
            print(f""" 
                                {telefonoContacto}""")
    else:
        print(f"No existe registro RUT: {personalRut}")
        
def modificarMiRegistro(peronalRut):
    print(f"""
                        Modificar Mi Registro
            ( Dejar en blanco los atributos que no quiera modificar )
          """)
    # Registro Usuario Para que Elija que datos modificar
    miRegistro(personalRut=peronalRut)

    modificar_datos_personales = input("Quiere modificar algún dato personal? [s/n] > ").lower()
    if modificar_datos_personales == "s":
        # Modificar Datos Personales
        personalNuevoNombre = input("Nombre: ")
        personalNuevaDireccion = input("Direccion: ")
        personalNuevoGenero = input("Género: ")
    
    modificar_telefono = input("Desea modificar algún telefono? (s/n)").lower()
    if modificar_telefono == "s":
        # Modoficar Telefono
        telefono_modificar = input("Número a modificar: ")
        nuevo_telefono = input("Número nuevo: ")
        telefonoPersonalNuevo = {
                                    "telefono":telefono_modificar,
                                    "nuevoTelefono":nuevo_telefono
                                }
    mod_or_add_contacto = input("Quiere Agregar o Eliminar algún Contacto? [s/n] > ").lower()
    if mod_or_add_contacto == "s":
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
            contactoNombre = input("Nombre: ")
            contactoRelacionPersonal = input("Relacion con Personal: ")
            telefonoContactoNumeros = []
            agregar_telefonoContacto = "s"
            while agregar_telefonoContacto == "s":
                telefonoContacto = input("Número de Telefono: +569 ")
                telefonoContactoNumeros.append(telefonoContacto)
                agregar_telefonoContacto = input("Desea agregar otro telefono? [s/n]").lower()

        elif opcion == 2:
            contactoRut = input("Ingrese RUT Contacto a Eliminar: ")
            resultado_eliminar_contacto = dtoPersonal().eliminarContacto(contactoRut=contactoRut)
            return resultado_eliminar_contacto if resultado_eliminar_contacto is not None else None
        elif opcion == 3:
            pass
        else:
            pass
        
    mod_or_add_carga = input("Quiere Agregar o Eliminar alguna Carga? [s/n] > ")
    if mod_or_add_carga == "s":
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
            
            resultado_add_carga = dtoPersonal().modificarMiRegistro()
            
        elif opcion == 2:
            cargaRut = input("Ingrese RUT Carga: ")
            resultado_eliminar_carga = dtoPersonal().modificarMiRegistro()
            return resultado_eliminar_carga if resultado_eliminar_carga is not None else None
        elif opcion == 3:
            pass
        else:
            pass
        
    resultado = dtoPersonal().modificarMiRegistro(
        personaRut=peronalRut, personalNombre=personalNuevoNombre,
        personalGenero=personalNuevoGenero, personalDireccion=personalNuevaDireccion)
    return resultado if resultado is not None else None

def menuMiRegistro(personalRut):
    salir = "n"
    while salir == "n":
        print(f"""
                1. Ver Registro ✅
                2. Modificar Mi Registro ❌
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
        