import sqlite3

class Database():

    def __init__(self):
        # get user input for self.__dbpath
        print(chr(27) + "[2J")
        self.__dbpath = input("Enter name of database file: ")
        self.connection = sqlite3.connect(self.__dbpath)
        self.cursor = self.connection.cursor()
        self.cursor.execute(' PRAGMA foreign_keys = ON; ')
        self.connection.commit()
        print("Connected to database.")

    def getInputTable(self):
        query = "SELECT * FROM InputRelationSchemas"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def nameExists(self,name):
        query = "SELECT * FROM InputRelationSchemas WHERE Name = ?"
        self.cursor.execute(query, (name,))
        if self.cursor.fetchall():
            return True
        else:
            return False

    def getFD(self, name):
        query = "SELECT FDs FROM InputRelationSchemas WHERE Name = ?"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()
