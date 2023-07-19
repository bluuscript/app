import sys
sys.path.append(".")

from conn.conn import ConectarBD

class daoPersonal:
    
    def __init__(self):
        
        try:
            self.conn = ConectarBD("localhost", "root", "", "testnomina")
        except Exception as error:
            print(f"conn daoPersonal error: {error}")
        self.cursor = self.conn.getCursor()
    def getConn(self):
        return self.conn
    
    # Faltan Tablas ❗
    def getMiRegistro(self, Personal):
        sql_registroPersonal = """SELECT `personalRut`, `personalNombre`, `personalGenero`, `personalDireccion`,
            `cargoNombre`, `cargoFechaIngreso`, `departamentoNombre`, `areaNombre`
            FROM `personal` P JOIN `cargo` C ON P.cargoID = C.cargoID
            JOIN `departamento` D on P.departamentoID = D.departamentoID JOIN
            `area` A on P.areaID = A.areaID WHERE `personalRut` = %s"""
        # Consultar Telefonos de Personal
        sql_personalTelefonos = """SELECT telefonoPersonalNumero FROM telefonosPersonal
            WHERE personalRutDueñoNumero = %s"""
        # Consultar Cargas del Personal según personalRut
        sql_registroCargas = """SELECT cargaRut, cargaNombre, cargaGenero, cargaParentesco
            FROM cargas WHERE personalRutRelacionCarga = %s"""
        # Consultar Contactos de Emergencia del Personal según personalRut --probar❗
        sql_registroContactos = """SELECT contactoNombre, contactoRelacionConPersonal WHERE personalRutContacto = %s"""
        # Consultar telefonos de contactos según contactoID = telefonoContactoID --probar❗
        sql_contactosTelefonos = """SELECT telefonoContactoNumero FROM telefonosContacto
            JOIN contactos ON personalContactoID = contactoID WHERE personalRutContacto = %s"""

        try:
            self.cursor.execute(sql_registroPersonal, (Personal.personalRut,))
            personal = self.cursor.fetchone()
            
            self.cursor.execute(sql_personalTelefonos, (Personal.personalRut,))
            personalTelefonos = self.cursor.fetchall()
            
            self.cursor.execute(sql_registroCargas, (Personal.personalRut,))
            personalCargas = self.cursor.fetchall()
            
            self.cursor.execute(sql_registroContactos, (Personal.personalRut,))
            personalContactos = self.cursor.fetchall()
            
            self.cursor.execute(sql_contactosTelefonos, (Personal.personalRut,))
            contactoTelefonos = self.cursor.fetchall()

        except Exception as error:
            print(f"Obtener Mi registro, error: {error}")
        return personal, personalTelefonos, personalCargas, personalContactos, contactoTelefonos
    
    # Faltan Tablas ❗
    def modificarMiRegistro(self, Personal):
        sql_Personal = "UPDATE `personal` SET `personalNombre`=%s, `personalGenero`=%s, \
            `personalDireccion`=%s WHERE `personalRut`=%s"
        # Modificar Cargas, Contactos - telefonosContacto, telefonosPersonal
        # Modificar Cargas del Personal 
        sql_Cargas = "UPDATE `cargas` SET `cargaRut`=%s, `cargaNombre`=%s, \
            `cargaParentesco`=%s, `cargaGenero`=%s WHERE `personalRutRelacionCarga=%s`"
        # Modificar Contactos Personal
        sql_Contactos = "UPDATE `contactos` "
        try:
            # Se modifica registro en Tabla => Personal
            self.cursor.execute(sql_Personal, (Personal.personalNombre, Personal.personalGenero,\
                Personal.personalDireccion, Personal.personalRut,))
            # Modificar Cargas
            self.cursor.execute(sql_Cargas, (Personal.atributos,))
            # Modificar Departamento
            self.conn.getConn().commit()
        except Exception as error:
            print(error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()