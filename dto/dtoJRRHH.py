import sys
sys.path.append(".")

from dao.daoJRRHH import daoJRRHH
from modelo.personal import Personal
from dto.dtoRRHH import dtoRRHH

class dtoJRRHH(dtoRRHH):
    # ✅
    def registrosNominaFiltro(self, personalGenero="", cargoNombre="", areaNombre="", departamentoNombre=""):
        
        resultado_filtro = daoJRRHH().getRegistrosFiltro(Personal=Personal(
                                    personalGenero=personalGenero, cargaNombre=cargoNombre,
                                    areaNombre=areaNombre, departamentoNombre=departamentoNombre))
        
        return resultado_filtro if resultado_filtro is not None else "Filtro sin Resultado"

# Pruebas:

#test_filtro_dto = dtoJRRHH().registrosNominaFiltro(personalGenero="m")
#print(test_filtro_dto)