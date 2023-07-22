import mysql.connector

class ConectarBD:
    def __init__(self,  host, user, passwd, database):
        try:
            self.__myconn=mysql.connector.connect(host=host, \
                                             user=user, \
                                             passwd=passwd, \
                                             database=database)
        except Exception as ex:
            print(ex)
            self.__myconn.rollback()
            
    def getConn(self):
        return self.__myconn
    
    def closeConn(self):
        self.__myconn.close()

    def getCursor(self):
        return self.__myconn.cursor(buffered=True)