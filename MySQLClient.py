import mysql.connector

class MySQLClient:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(host = host,
             user = user,
             password = password,
             database = database,
             auth_plugin='mysql_native_password')

    def converByteStringToString(self,byteString):
        return byteString.decode("utf-8")

    # Queries for databases
    def showDatabases(self):
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("SHOW DATABASES")
        return cursor.fetchall()

    def useDatabase(self,dbName):
        # Enter to database
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("USE {}".format(dbName))
        print('Database entering is successful')

    def showTables(self,dbName):
        # Show tabales inside the database
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('USE {}'.format(dbName))
        cursor.execute('SHOW TABLES')
        return cursor.fetchall()

    def readDataFromTable(self,dbName,tableName):
        # Read data from a table
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('SELECT * FROM {}.{}'.format(dbName,tableName))
        return cursor.fetchall()

dbObj = MySQLClient('10.0.0.21','rbt','rbt.1234','anushan')

print(dbObj.readDataFromTable('anushan','uploaded_contents')[-1])

