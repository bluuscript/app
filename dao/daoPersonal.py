import sys
sys.path.append(".")

from conn.conn import ConectarBD
from modelo.personal import Personal

class daoPersonal:
    
    def __init__(self):
        
        try:
            self.conn = ConectarBD("localhost", "root", "", "testnomina")
        except Exception as error:
            print(f"conn daoPersonal error: {error}")
        self.cursor = self.conn.getCursor()
    def getConn(self):
        return self.conn
    
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
        # Consultar Contactos de Emergencia del Personal según personalRut
        sql_registroContactos = """SELECT contactoRut, contactoNombre, contactoRelacionConPersonal, contactoID FROM contactos WHERE personalRutContacto = %s"""
        # Consultar telefonos de contactos según contactoID = telefonoContactoID --probar❗
        sql_contactosTelefonos = """SELECT telefonoContactoNumero FROM telefonosContacto
            JOIN contactos ON telefonoContactoID = contactoID WHERE telefonoContactoID = %s"""

        try:
            self.cursor.execute(sql_registroPersonal, (Personal.personalRut,))
            self.conn.getConn().commit()
            personal = self.cursor.fetchone()
            
            self.cursor.execute(sql_personalTelefonos, (Personal.personalRut,))
            self.conn.getConn().commit()
            personalTelefonos = self.cursor.fetchall()
            
            self.cursor.execute(sql_registroCargas, (Personal.personalRut,))
            self.conn.getConn().commit()
            personalCargas = self.cursor.fetchall()
            
            self.cursor.execute(sql_registroContactos, (Personal.personalRut,))
            personalContactos = self.cursor.fetchall()
            self.conn.getConn().commit()
            
            contactoTelefonos = []
            for contacto in personalContactos:
                self.cursor.execute(sql_contactosTelefonos, (contacto[3],))
                contactoTelefonos.append({
                    "contactoID": contacto[3],
                    "telefonosContacto": self.cursor.fetchall()
                })

        except Exception as error:
            print(f"Obtener Mi registro, error: {error}")
        return personal, personalTelefonos, personalCargas, personalContactos, contactoTelefonos
    
    def existeRegistro(self, Personal):
        try:
            self.cursor.execute("""SELECT personalRut FROM personal WHERE personalRut = %s""", (Personal.personalRut,))
        except Exception as ex:
            print("Existe Registro, error:", ex)
        return self.cursor.fetchone()
    
    def modificarMiRegistro(self, Personal):
        sql_Personal = """UPDATE personal SET personalNombre=%s, personalGenero=%s,
            personalDireccion=%s WHERE personalRut=%s"""
        try:
            # Se modifica registro en Tabla => Personal
            self.cursor.execute(sql_Personal, (Personal.personalNombre, Personal.personalGenero,
                Personal.personalDireccion, Personal.personalRut,))
            self.conn.getConn().commit()
            if self.cursor.rowcount > 0:
                print(f"Registro {Personal.personalRut} Modificado")
            else:
                print(f"Error al Modificar Personal {Personal.personalRut}")
        except Exception as error:
            print("modificarMiRegistro(), error:", error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
    
    def agregarContacto(self, Personal):
        # Consulta para Insertar Contactos Personal
        sql_agregarContacto="""INSERT INTO contactos ( contactoID, contactoRut, contactoNombre, contactoRelacionConPersonal, personalRutContacto)
            VALUES (%s,%s,%s,%s,%s)"""
        # Consulta para Insertar Telefonos del Contacto
        sql_insertarTelefonosContacto = """INSERT INTO telefonosContacto (telefonoContactoNumero, telefonoContactoID)
            VALUES (%s,%s)"""
        try:
             # Ejecutar consulta insertar contactos
            self.cursor.execute(sql_agregarContacto, (Personal.contactoID, Personal.contactoRut, Personal.contactoNombre, Personal.contactoRelacionPersonal, Personal.personalRut,))
            self.conn.getConn().commit()
            # Insertar cada telefono contacto:
            for telefonoContacto in Personal.telefonoContactoNumeros:
                self.cursor.execute(sql_insertarTelefonosContacto, (telefonoContacto, Personal.contactoID,))
                self.conn.getConn().commit()
        except Exception as error:
            print("agregarContacto(), error: ", error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
                
    def eliminarContacto(self, Personal):
        sql_eliminarContactos ="DELETE FROM `contactos` WHERE contactoRut=%s"
        sql_eliminarContactosTelefonos = """DELETE T.* FROM telefonosContacto T
            JOIN contactos C ON telefonoContactoID = contactoID WHERE contactoRut=%s""" 
        try:
            self.cursor.execute(sql_eliminarContactosTelefonos, (Personal.contactoRut,))
            self.conn.getConn().commit()
            self.cursor.execute(sql_eliminarContactos, (Personal.contactoRut,))
            self.conn.getConn().commit()
            if self.cursor.rowcount > 0:
                print(f"Contacto {Personal.contactoRut} Eliminado")
            else:
                print(f"Error al Eliminar Contacto {Personal.contactoRut}")
        except Exception as error:
            print("eliminarContacto(), error: ", error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()
                
    def agregarCarga(self, Personal):
        # Consulta para Insertar Cargas
        sql_insertarCarga = """INSERT INTO cargas (cargaRut, cargaNombre, cargaParentesco, cargaGenero, personalRutRelacionCarga)
            VALUES (%s,%s,%s,%s,%s)"""
        try:
             # Ejecutar consulta insertar Carga
            self.cursor.execute(sql_insertarCarga, (Personal.cargaRut, Personal.cargaNombre, Personal.cargaParentesco,
                                                Personal.cargaGenero, Personal.personalRut,))
            self.conn.getConn().commit()
        except Exception as error:
            print("agregarCarga(), error: ", error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()

    def eliminarCarga(self, Personal):
        sql_eliminarCarga = "DELETE FROM `cargas` WHERE `cargaRut`=%s"
        try:
            self.cursor.execute(sql_eliminarCarga, (Personal.cargaRut,))
            self.conn.getConn().commit()
        except Exception as error:
            print("eliminarCarga(), error: ", error)
        finally:
            if self.conn.getConn().is_connected():
                self.conn.closeConn()

#print(daoPersonal().getMiRegistro(Personal=Personal(personalRut="1-1")))