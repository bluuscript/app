import sys
sys.path.append(".")
from modelo.personal import Personal
from dao.daoPersonal import daoPersonal

class dtoPersonal:
    
    def miRegistro(self, personalRut):
        # Obtener Registro mediante class daoPersonal()
        registro = daoPersonal().getMiRegistro(Personal=Personal(personalRut=personalRut))
        
        return registro if registro is not None else None
    
    def modificarMiRegistro(self, personaRut, personalNombre, personalGenero, personalDireccion, telefonoPersonalNumero,
            contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros, cargaRut, cargaNombre, cargaParentesco, cargaGenero):
        resultado = daoPersonal().modificarMiRegistro(
            Personal=Personal(
                personalRut=personaRut, personalNombre=personalNombre, personalGenero=personalGenero,
                personalDireccion=personalDireccion, telefonoPersonalNumero=telefonoPersonalNumero,
                contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros,
                cargaRut=cargaRut, cargaNombre=cargaNombre, cargaParentesco=cargaParentesco, cargaGenero=cargaGenero
            )
        )
        return resultado if resultado is not None else None