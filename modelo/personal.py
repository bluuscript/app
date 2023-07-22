# date para generar fecha ingreso personal a la empresa
from datetime import date
# uuid para generar IDs Tablas: Cargo, Departamento, Area y Contactos de Emergencia
from uuid import uuid1


class Cargo:
    def __init__(self, cargoNombre, cargoFechaIngreso=""):
        self.cargoID = str(uuid1())
        self.cargoNombre = cargoNombre
        self.cargoFechaIngreso = cargoFechaIngreso
        
    def __str__(self):
        return f"Cargo: {self.cargoNombre} - Fecha de Ingreso: {self.cargoFechaIngreso}"
        
class Departamento:
    def __init__(self, departamentoNombre):
        self.departamentoID = str(uuid1())
        self.departamentoNombre=departamentoNombre
        
    def __str__(self):
        return f"Departamento: {self.departamentoNombre}"

class Area:
    def __init__(self, areaNombre):
        self.areaID= str(uuid1())
        self.areaNombre=areaNombre
        
    def __str__(self):
        return f"Area: {self.areaNombre}"
        
class TelefonosContacto:
    def __init__(self, telefonoContactoNumeros):
        self.telefonoContactoNumeros = telefonoContactoNumeros
        
    def __str__(self):
        return f" · {self.telefonoContactoNumeros}"
        
class ContactosEmergencia(TelefonosContacto):
    def __init__(self, contactoID=str(uuid1()), contactoRut="", contactoNombre = "", contactoRelacionPersonal = "", telefonoContactoNumeros = []):
        TelefonosContacto.__init__(self, telefonoContactoNumeros)
        self.contactoID = contactoID
        self.contactoRut = contactoRut
        self.contactoNombre = contactoNombre
        self.contactoRelacionPersonal = contactoRelacionPersonal
        self.telefonoContactoNumeros = telefonoContactoNumeros
        
    def __str__(self):
        return f"· RUT: {self.contactoRut} - Nombre: {self.contactoNombre} - Relacion: {self.contactoRelacionPersonal}"
    
    def strTelefonos(self):
        return f"· {self.telefonoContactoNumeros}"
    
class CargasFamiliares:
    def __init__(self, cargaRut, cargaNombre, cargaParentesco, cargaGenero):
        self.cargaRut = cargaRut
        self.cargaNombre = cargaNombre
        self.cargaParentesco = cargaParentesco
        self.cargaGenero = cargaGenero
        
    def __str__(self):
        return f"· RUT: {self.cargaRut} - Nombre: {self.cargaNombre} - Género: {self.cargaGenero} - Parentesco: {self.cargaParentesco}"

class TelefonosPersonal:
    def __init__(self, telefonoPersonalNumeros):
        self.telefonoPersonalNumeros = telefonoPersonalNumeros
        
    def __str__(self):
        return f" · {self.telefonoPersonalNumeros}"
            
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
                    contactoID=str(uuid1()), contactoRut="", contactoNombre="", contactoRelacionPersonal="", telefonoContactoNumeros=[]
                    ):
        
        Cargo.__init__(self, cargoNombre, cargoFechaIngreso)
        Departamento.__init__(self, departamentoNombre)
        Area.__init__(self, areaNombre)
        
        TelefonosPersonal.__init__(self, telefonoPersonalNumeros)

        CargasFamiliares.__init__(self, cargaRut, cargaNombre, cargaParentesco,  cargaGenero)
        ContactosEmergencia.__init__(self, contactoID, contactoRut, contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros)
        
        self.personalRut = personalRut
        self.personalNombre = personalNombre
        self.personalGenero = personalGenero
        self.personalDireccion = personalDireccion

    def __str__(self):
        # Resumen Personal
        return f"\n\tRUT: {self.personalRut} - Nombre: {self.personalNombre} - Género: {self.personalGenero} - Cargo: {self.cargoNombre}"

    def datosPersonales(self):
        # Datos Personales 
        return f"\n\tRUT: {self.personalRut} - Nombre: {self.personalNombre} - Género: {self.personalGenero} - Dirección: {self.personalDireccion}"
