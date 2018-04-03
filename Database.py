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
        FDs = set()
        for fd in (self.cursor.fetchone()[0] + ';').split(" "):
            FDs.add(fd)
        return FDs

    def getAttributes(self, name):
        query = "SELECT Attributes FROM InputRelationSchemas WHERE Name = ?"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()[0]

    def getFDSetList(self,name):
        fds = self.getFD(name)
        lst = list()
        for fd in fds:
            temp = fd.replace("{","")
            temp = temp.replace("}","")
            temp = temp.replace(";","")
            lst.append(temp.split("=>"))
        for fd in lst:
            fd[0] = set(fd[0].split(","))
            fd[1] = set(fd[1].split(","))
        return lst

    def getAttributeSet(self,name):
        return set(self.getAttributes(name).split(","))

    def outputNormalization(self,name,attributes,FDs):
        self.cursor.execute('''INSERT OR IGNORE INTO OutputRelationSchemas VALUES (?,?,?)''',(name,attributes,FDs))
        self.connection.commit()

    def addDecomposedTable(self,originalName,newName,table):
        self.cursor.execute('''PRAGMA table_info({})'''.format(originalName))
        allrows = self.cursor.fetchall()
        typeDict = dict()
        for row in allrows:
            typeDict[row[1]] = row[2]
            # print(row[1],row[2])
        
