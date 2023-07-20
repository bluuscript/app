# date para generar fecha ingreso personal a la empresa
from datetime import date
# uuid para generar IDs Tablas: Cargo, Departamento, Area y Contactos de Emergencia
from uuid import uuid1


class Cargo:
    def __init__(self, cargoNombre, cargoFechaIngreso=""):
        self.cargoID = str(uuid1())
        self.cargoNombre = cargoNombre
        self.cargoFechaIngreso = cargoFechaIngreso
        
    def printCargo(self):
        
        print(f"Cargo: {self.cargoNombre} - Fecha de Ingreso: {self.cargoFechaIngreso}")
        
class Departamento:
    def __init__(self, departamentoNombre):
        self.departamentoID = str(uuid1())
        self.departamentoNombre=departamentoNombre
        
    def printDepartamento(self):
        
        print(f"Nombre: {self.departamentoNombre}")

class Area:
    def __init__(self, areaNombre):
        self.areaID= str(uuid1())
        self.areaNombre=areaNombre
        
    def printArea(self):
        
        print(f"Nombre: {self.areaNombre}")
        
class TelefonosContacto:
    def __init__(self, telefonoContactoNumeros):
        self.telefonoContactoNumeros = telefonoContactoNumeros
        
    def printTelefonosContacto(self):
        
        print(f"\nTelefonos Contacto: {self.telefonoContactoNumeros}")
        
class ContactosEmergencia(TelefonosContacto):
    def __init__(self, contactoID=str(uuid1()), contactoNombre = "", contactoRelacionPersonal = "", telefonoContactoNumeros = ""):
        super().__init__(telefonoContactoNumeros)
        self.contactoID = contactoID
        self.contactoNombre = contactoNombre
        self.contactoRelacionPersonal = contactoRelacionPersonal
        self.telefonoContactoNumeros = telefonoContactoNumeros
        
    def printContactosEmergencia(self):
        print(f"\nNombre: {self.contactoNombre} - Relacion: {self.contactoRelacionPersonal} - Telefonos Contacto: {self.telefonoContactoNumeros}")
        
class CargasFamiliares:
    def __init__(self, cargaRut, cargaNombre, cargaParentesco, cargaGenero):
        self.cargaRut = cargaRut
        self.cargaNombre = cargaNombre
        self.cargaParentesco = cargaParentesco
        self.cargaGenero = cargaGenero
        
    def printCargasFamiliares(self):
        return f"\nRUT: {self.cargaRut} - Nombre: {self.cargaNombre} - Género: {self.cargaGenero} - Parentesco: {self.cargaParentesco}"

class TelefonosPersonal:
    def __init__(self, telefonoPersonalNumeros):
        self.telefonoPersonalNumeros = telefonoPersonalNumeros
        
    def printTelefonosPersonal(self):
        
        print(f"\nTelefonos Personal: {self.telefonoPersonalNumeros}")
            
class Personal(Cargo, Departamento, Area, TelefonosPersonal, CargasFamiliares, ContactosEmergencia):
    
    def __init__(self,
                    #Tabla Personal
                    personalRut="", personalNombre="", personalGenero="", personalDireccion="",
                    # Tabla Cargo
                    cargoNombre="", cargoFechaIngreso="",
                    # Tabla Departamento
                    departamentoNombre="", areaNombre="",
                    # Tabla TelefonosPersonal
                    telefonoPersonalNumeros=[],
                    # Tabla CargasFamiliares
                    cargaRut="", cargaNombre="", cargaGenero="", cargaParentesco="",
                    # Tabla ContactosEmergencia
                    contactoNombre="", contactoRelacionPersonal="", telefonoContactoNumeros=[]
                    ):
        
        Cargo.__init__(self, cargoNombre, cargoFechaIngreso)
        Departamento.__init__(self, departamentoNombre)
        Area.__init__(self, areaNombre)
        
        TelefonosPersonal.__init__(self, telefonoPersonalNumeros)

        CargasFamiliares.__init__(self, cargaRut, cargaNombre, cargaParentesco,  cargaGenero)
        ContactosEmergencia.__init__(self, contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros)
        
        self.personalRut = personalRut
        self.personalNombre = personalNombre
        self.personalGenero = personalGenero
        self.personalDireccion = personalDireccion

    def __str__(self):
        # Resumen Personal
        return f"\n\tRUT: {self.personalRut} - Nombre: {self.personalNombre} - Género: {self.personalGenero} - Cargo: {self.cargoNombre}"
