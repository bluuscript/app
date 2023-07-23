import sys
sys.path.append(".")

from dao.daoJRRHH import daoJRRHH
from modelo.personal import Personal
from dto.dtoRRHH import dtoRRHH

class dtoJRRHH(dtoRRHH):

    def registrosNominaFiltro(self, personalGenero="", cargoNombre="", areaNombre="", departamentoNombre=""):
        
        resultado_filtro = daoJRRHH().getRegistrosFiltro(Personal=Personal( 
                                    personalGenero=personalGenero, cargoNombre=cargoNombre,
                                    areaNombre=areaNombre, departamentoNombre=departamentoNombre))
        lista_registros=[]
        if resultado_filtro is not None:
            for registro in resultado_filtro:
                registro_personal=Personal(
                    personalRut=registro[0], personalNombre=registro[1],
                    personalGenero=registro[2], cargoNombre=registro[3],
                    areaNombre=registro[4], departamentoNombre=registro[5]
                    )
                lista_registros.append(registro_personal)
        return lista_registros if lista_registros is not None else None