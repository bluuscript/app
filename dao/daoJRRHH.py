import sys
sys.path.append(".")

from dao.daoRRHH import daoRRHH

class daoJRRHH(daoRRHH):

    def getRegistrosFiltro(self, Personal):
        sql_filtrarNomina = """SELECT `personalRut`, `personalNombre`, `personalGenero`,
            `cargoNombre`, `areaNombre`, `departamentoNombre`
            FROM `personal` P JOIN `cargo` C ON P.cargoID = C.cargoID 
            JOIN `departamento` D on P.departamentoID = D.departamentoID JOIN 
            `area` A on P.areaID = A.areaID 
            WHERE `personalGenero` LIKE %s AND `cargoNombre` LIKE %s 
            AND areaNombre LIKE %s AND departamentoNombre LIKE %s LIMIT 10"""
        try:
            self.cursor.execute(sql_filtrarNomina, ("%"+Personal.personalGenero+"%", "%"+Personal.cargoNombre+"%", "%"+Personal.areaNombre+"%", "%"+Personal.departamentoNombre+"%",))
        except Exception as ex:
            print(ex)
        return self.cursor.fetchall()

