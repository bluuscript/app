import sys
sys.path.append(".")
from dto.dtoPersonal import dtoPersonal

def miRegistro(personalRut):

    mi_registro = dtoPersonal().miRegistro(personalRut=personalRut)
    
    if mi_registro is not None:
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
                            {contacto}""")
    else:
        print(f"No existe registro RUT: {personalRut}")
        
def modificarMiRegistro(peronalRut):
    print(f"""
                        Modificar Mi Registro
            ( Dejar en blanco los atributos que no quiera modificar )
          """)
    # Modificar Datos Personales
    perosnalNuevoNombre = input("Nombre: ")
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
    modificar_carga = input("Desea modificar alguna Carga? (s/n)")
    if modificar_carga == "s":
        # Modificar Carga
        print("\nModificar Carga")
        cargaRut = input("Rut carga a modificar: ")
        cargaNuevoNombre = input("Nombre: ")
        cargaNuevoGenero = input("Género: ")
        cargaNuevoParentesco = input("Parentesco: ")
    
    modificar_contacto = input("Desea Modificar Algún Contacto de Emergencia? (s/n) ").lower()
    if modificar_contacto == "s":
        # Modificar Contacto
        print("\nModificar Contacto de Emergencia")
        contactoRut = input("Rut del Contacto a Modificar: ")
        contactoNuevoNombre = input("Nombre: ")
        contacoNuevoRelacionPersonal = input("Relacion: ")
        
        contacto_telefono_modificar = input("Número contacto a modificar: ")
        nuevo_telefono_contacto = input("Número nuevo: ")
        contactoTelefonoNuevo = {
                                    "telefonoContacto":contacto_telefono_modificar, 
                                    "telefonoContactoNuevo":nuevo_telefono_contacto
                                }
    
    resultado = dtoPersonal().modificarMiRegistro(
        personaRut=peronalRut, personalNombre=perosnalNuevoNombre,
        personalGenero=personalNuevoGenero, personalDireccion=personalNuevaDireccion,
        telefonoPersonalNumero=telefonoPersonalNuevo,
        cargaRut=cargaRut, cargaNombre=cargaNuevoNombre, cargaGenero=cargaNuevoGenero, cargaParentesco=cargaNuevoParentesco,
        contactoNombre=contactoNuevoNombre, contactoRelacionPersonal=contacoNuevoRelacionPersonal,
        telefonoContactoNumeros=contactoTelefonoNuevo
        )
    return resultado if resultado is not None else None

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
        salir = input("\nDesea Salir de Mi Registro? [s/n] > ")
        