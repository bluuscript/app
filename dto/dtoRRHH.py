import sys
sys.path.append(".")
from modelo.personal import *
from dao.daoRRHH import daoRRHH

class dtoRRHH:

    def agregarPersonalNomina(self,
                        personalNombre, personalRut, personalGenero, personalDireccion, 
                        telefonoPersonalNumeros,
                        cargoNombre, cargoFechaIngreso,
                        areaNombre, departamentoNombre,
                        cargaNombre, cargaParentesco, cargaGenero, cargaRut,
                        contactoRut, contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros
                        ):
        
        resultado_agregar = daoRRHH().addPersonal(Personal(personalNombre=personalNombre, personalRut=personalRut, personalGenero=personalGenero, personalDireccion=personalDireccion,
                                    telefonoPersonalNumeros=telefonoPersonalNumeros, cargoNombre=cargoNombre, cargoFechaIngreso=cargoFechaIngreso,
                                    areaNombre=areaNombre,departamentoNombre=departamentoNombre,
                                    contactoRut=contactoRut, contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal,telefonoContactoNumeros=telefonoContactoNumeros,
                                    cargaNombre=cargaNombre, cargaParentesco=cargaParentesco, cargaGenero=cargaGenero, cargaRut=cargaRut))
        return resultado_agregar if resultado_agregar is not None else None

    def registrosNomina(self):
        registros = daoRRHH().getRegistros()
        lista_registros=[]
        if registros is not None:
            for registro in registros:
                registro_personal=Personal(
                    personalRut=registro[0], personalNombre=registro[1],
                    personalGenero=registro[2], cargoNombre=registro[3]
                    )
                lista_registros.append(registro_personal)
        return lista_registros if lista_registros is not None else None
    
    def buscarRegistro(self, personalRut):
        
        resultado = daoRRHH().getOneRegistro(Personal=Personal(personalRut=personalRut))
        
        personal = Personal(
                personalRut=resultado[0], personalNombre=resultado[1],personalGenero=resultado[2],
                cargoNombre=resultado[3]
            )
        return True if resultado is not None else None
    
    def modificarDatosLaborales(self, personalRut, cargoNombre, cargoFechaIngreso, departamentoNombre, areaNombre):
        resultado = daoRRHH().updateLaboral(Personal(personalRut = personalRut, cargoNombre = cargoNombre, cargoFechaIngreso = cargoFechaIngreso, departamentoNombre =  departamentoNombre, areaNombre = areaNombre))
        return resultado if resultado is not None else None
       
    def modificarPersonal(self, personalRut, personalNombre, personalGenero, personalDireccion):
        
        resultado_modificar = daoRRHH().updatePersonal(Personal(personalNombre=personalNombre, personalRut=personalRut, personalGenero=personalGenero, personalDireccion=personalDireccion))
        return resultado_modificar if resultado_modificar is not None else None
    
    def agregarContacto(self, personalRut, contactoRut, contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros):
        resultado = daoRRHH().agregarContacto(
            Personal=Personal(
                personalRut=personalRut, contactoRut=contactoRut, contactoNombre=contactoNombre,
                contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros
            )
        )
        return resultado if resultado is not None else None
    
    def eliminarContacto(self, contactoRut):
        resultado = daoRRHH().eliminarContacto(Personal=Personal(contactoRut=contactoRut))
        return resultado if resultado is not None else None
    
    def agregarCarga(self, personalRut, cargaRut, cargaNombre, cargaGenero, cargaParentesco):
        resultado = daoRRHH().agregarCarga(
            Personal=Personal(
                cargaRut=cargaRut, cargaNombre=cargaNombre,
                cargaGenero=cargaGenero, cargaParentesco=cargaParentesco,
                personalRut=personalRut
            )
        )
        return resultado if resultado is not None else None
    
    def eliminarCarga(self, cargaRut):
        resultado = daoRRHH().eliminarCarga(Personal=Personal(cargaRut=cargaRut))
        return resultado if resultado is not None else None

    def eliminarPersonal(self, personalRut):
        
        resultado_eliminar = daoRRHH().deletePersonal(Personal=Personal(personalRut=personalRut))
        return resultado_eliminar if resultado_eliminar is not None else None 
            