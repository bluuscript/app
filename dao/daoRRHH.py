import sys
sys.path.append(".")

from conn.conn import ConectarBD

# Se usa como tipo
from modelo.personal import Personal

class daoRRHH:
    def __init__(self):
        try:
            self.conn= ConectarBD("localhost", "root", "", "testnomina")
        except Exception as ex:
            print(ex)
        self.cursor = self.conn.getCursor()

    def getConn(self):
        return self.conn
    
    def addPersonal(self, Personal:Personal):
        sql_insertarCargo = "INSERT INTO `cargo` (`cargoID`, `cargoNombre`, `cargoFechaIngreso`) \
            VALUES (%s,%s,%s)"
        sql_insertarDepartamento = "INSERT INTO `departamento` (`departamentoID`, `departamentoNombre`) \
            VALUES (%s,%s)"
        sql_insertarArea = "INSERT INTO `area` (`areaID`, `areaNombre`) \
            VALUES (%s,%s)"
        sql_insertarPersonal = "INSERT INTO `personal` (`personalRut`, `personalNombre`, \
            `personalGenero`, `personalDireccion`, `cargoID`, `departamentoID`, `areaID`) \
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
        sql_insertarTelefonosPersonal = "INSERT INTO `telefonosPersonal` (`telefonoPersonalNumero`, `personalRutDueñoNumero`) \
            VALUES (%s,%s)"
        # Consulta para Insertar Cargas
        sql_insertarCargas = """INSERT INTO cargas (cargaRut, cargaNombre, cargaParentesco, cargaGenero, personalRutRelacionCarga)
            VALUES (%s,%s,%s,%s,%s)"""
        # Consulta para Insertar Contactos Personal
        sql_insertarContactos = """INSERT INTO contactos ( contactoID, contactoRut, contactoNombre, contactoRelacionConPersonal, personalRutContacto)
            VALUES (%s,%s,%s,%s,%s)"""
        # Consulta para Insertar Telefonos Contacto
        sql_insertarTelefonosContacto = """INSERT INTO telefonosContacto (telefonoContactoNumero, telefonoContactoID)
            VALUES (%s,%s)""" 
        try:
            self.cursor.execute(sql_insertarCargo, (Personal.cargoID, Personal.cargoNombre, Personal.cargoFechaIngreso,))
            self.cursor.execute(sql_insertarDepartamento, (Personal.departamentoID, Personal.departamentoNombre,))
            self.cursor.execute(sql_insertarArea, (Personal.areaID, Personal.areaNombre,))
            self.cursor.execute(sql_insertarPersonal, (Personal.personalRut, Personal.personalNombre, 
                            Personal.personalGenero, Personal.personalDireccion, Personal.cargoID, Personal.departamentoID, Personal.areaID,))
            self.conn.getConn().commit()
            # Insertar cada telefono del personal como lista
            for telefono in Personal.telefonoPersonalNumeros: 
                self.cursor.execute(sql_insertarTelefonosPersonal, (telefono, Personal.personalRut,))
                self.conn.getConn().commit()
            # Ejecutar consulta insertar cargas
            self.cursor.execute(sql_insertarCargas, (Personal.cargaRut, Personal.cargaNombre, Personal.cargaParentesco, Personal.cargaGenero, Personal.personalRut,))
            # Ejecutar consulta insertar contactos
            self.cursor.execute(sql_insertarContactos, (Personal.contactoID, Personal.contactoRut, Personal.contactoNombre, Personal.contactoRelacionPersonal, Personal.personalRut,))
            self.conn.getConn().commit()
            # Insertar cada telefono contacto:
            for telefonoContacto in Personal.telefonoContactoNumeros:
                self.cursor.execute(sql_insertarTelefonosContacto, (telefonoContacto, Personal.contactoID,))
                self.conn.getConn().commit()
            
            if self.cursor.rowcount > 0:
                print(f"Personal {Personal.personalRut} Agregado")
            else:
                print(f"Error al Agregar {Personal.personalRut}")
        except Exception as error:
            print(error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
    
    def getRegistros(self):
        try:
            self.cursor.execute(
            """SELECT `personalRut`, `personalNombre`, `personalGenero`,
            `cargoNombre` FROM `personal` P JOIN `cargo` C ON P.cargoID = C.cargoID
            JOIN `departamento` D on P.departamentoID = D.departamentoID JOIN 
            `area` A on P.areaID = A.areaID""")
        except Exception as ex:
            print(ex)
        return self.cursor.fetchall()
    
    def getOneRegistro(self, Personal):
        try:
            self.cursor.execute(
            """SELECT `personalRut`, `personalNombre`, `personalGenero`,
            `cargoNombre` FROM `personal` P JOIN `cargo` C ON P.cargoID = C.cargoID
            JOIN `departamento` D on P.departamentoID = D.departamentoID JOIN 
            `area` A on P.areaID = A.areaID WHERE personalRut = %s""", (Personal.personalRut,))
        except Exception as ex:
            print("getOneRegistro error:", ex)
        return self.cursor.fetchone()
    
    def updatePersonal(self, Personal):
        sql_personal="UPDATE `personal` SET `personalNombre`=%s, `personalGenero`=%s, `personalDireccion`=%s \
            WHERE `personalRut`=%s"
        # Modificar Cargo, Departamento y Area del Personal
        sql_cargo = ""  
        sql_departamento = ""
        sql_area = ""
        # Modificar Cargas, Contactos - telefonosContacto, telefonosPersonal 
        try:
            # Se modifica solo registro en talbla => personal
            self.cursor.execute(sql_personal,(Personal.personalNombre, Personal.personalGenero,\
                Personal.personalDireccion, Personal.personalRut,))
            self.conn.getConn().commit()
        except Exception as error:
            print(error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
    
    def deletePersonal(self, Personal):
                
        sql_eliminarPersonal ="DELETE FROM `personal` WHERE `personalRut`=%s"
        sql_eliminarCargas = "DELETE FROM `cargas` WHERE `personalRutRelacionCarga`=%s"
        sql_eliminarTelefonos ="DELETE FROM `telefonosPersonal` WHERE `personalRutDueñoNumero`=%s"
                
        sql_eliminarContactos ="DELETE FROM `contactos` WHERE `personalRutContacto`=%s"
        #sql_eliminarContactosTelefonos = "DELETE FROM `telefonosContacto` WHERE \
        #    `telefonoContactoID`=%s"
        sql_eliminarContactosTelefonos = """DELETE T.* FROM telefonosContacto T
            JOIN contactos C ON telefonoContactoID = contactoID WHERE personalRutContacto=%s"""   
        sql_eliminarCargo = """DELETE FROM cargo WHERE cargoID = %s"""
        #sql_eliminarCargo = "DELETE FROM cargo WHERE cargoID = (SELECT cargoID FROM personal WHERE personalRut = %s)"
        sql_eliminarDepartamento = """DELETE FROM departamento WHERE departamentoID = %s"""
        sql_eliminarArea = """DELETE FROM area WHERE areaID = %s"""
              
        try:
            self.cursor.execute(sql_eliminarContactosTelefonos, (Personal.personalRut,))
            self.conn.getConn().commit()
            self.cursor.execute(sql_eliminarContactos, (Personal.personalRut,))
            self.conn.getConn().commit()
            # Eliminar Registro Personal con RUT   
            self.cursor.execute(sql_eliminarTelefonos, (Personal.personalRut,))
            self.conn.getConn().commit()
            self.cursor.execute(sql_eliminarCargas, (Personal.personalRut,))
            self.conn.getConn().commit()
            self.cursor.execute("""SELECT cargoID, departamentoID, areaID FROM personal
                                WHERE personalRut = %s""", (Personal.personalRut,))
            laborales_IDs = self.cursor.fetchone()
            # Eliminar Registro Tabla Principal
            self.cursor.execute(sql_eliminarPersonal, (Personal.personalRut,))
            self.conn.getConn().commit()
            # Eliminar Registro Datos Laborales del Personal con ID:
            self.cursor.execute(sql_eliminarCargo, (laborales_IDs[0],))
            self.conn.getConn().commit()
            self.cursor.execute(sql_eliminarDepartamento, (laborales_IDs[1],))
            self.conn.getConn().commit()
            self.cursor.execute(sql_eliminarArea, (laborales_IDs[2],))
            self.conn.getConn().commit()
            
            print(f"Rut: {Personal.personalRut} eliminado exitosamente")
        except Exception as error:
            print(f"Error: {error} al eliminar Personal: {Personal.personalRut}")
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
