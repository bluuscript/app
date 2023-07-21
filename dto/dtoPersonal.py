import sys
sys.path.append(".")
from modelo.personal import Personal
from dao.daoPersonal import daoPersonal

class dtoPersonal:
    
    def miRegistro(self, personalRut):
        # Obtener Registro mediante class daoPersonal()
        registro = daoPersonal().getMiRegistro(Personal=Personal(personalRut=personalRut))
        
        personal = Personal(
            personalRut=registro[0],
            personalNombre=registro[1],
            personalGenero=registro[2],
            personalDireccion=registro[3],
            cargoNombre=registro[4],
            cargoFechaIngreso=registro[5],
            departamentoNombre=registro[6],
            areaNombre=registro[7]
        )
        
        return personal if personal is not None else None
    
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