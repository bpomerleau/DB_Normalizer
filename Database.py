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
        FDs = list()
        for fd in (self.cursor.fetchone()[0] + ';').split(" "):
            FDs.append(fd)
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

    def addDecomposedTables(self,originalName,tables,nameList):
        self.cursor.execute('''PRAGMA table_info({})'''.format(originalName))
        allrows = self.cursor.fetchall()
        typeDict = dict()
        for row in allrows:
            typeDict[row[1]] = [row[2],row[5]]
            # print(row[1],row[2])
        for index in range(len(tables)):
            table = tables[index]
            self.cursor.execute('''DROP TABLE IF EXISTS {}'''.format(nameList[index]))
            createStr = "CREATE TABLE " + nameList[index] + " ( "
            for attr in list(table[0]):
                createStr = createStr + attr +" "+typeDict[attr][0]+", "

            pkStr = "PRIMARY KEY ("
            primaryKey = ""
            keyList = list(table[0])
            count = 0
            for i in range(len(keyList)):
                if typeDict[keyList[i]][1]>0:
                    if count == 0:
                        pkStr = pkStr + keyList[i]
                        primaryKey = primaryKey + keyList[i]
                        count = count + 1
                        continue
                    pkStr = pkStr + "," + keyList[i]
                    primaryKey = primaryKey + "," + keyList[i]
                    count = count + 1
            pkStr = pkStr + ")"

            fpkStr = ""
            if index > 0 and len(keyList)>1:
                for fd in tables[index-1][1]:
                    if table[0].intersection(fd[0])>=fd[0]:
                        # fpkStr = ", FOREIGN KEY (" + table[0].intersection(fd[0]) + ") REFERENCES " + nameList[i-1]
                        fpkStr = ", FOREIGN KEY ("
                        sortedKeys = sorted(table[0].intersection(fd[0]))
                        for key in sortedKeys:
                            fpkStr = fpkStr + key
                        fpkStr = fpkStr + ") REFERENCES " + nameList[index-1]
            createStr = createStr + pkStr + fpkStr + ");"
            print(createStr)
            self.cursor.execute(createStr)
            self.connection.commit()

            attrList = sorted(table[0])
            insertStr = "INSERT OR REPLACE INTO " + nameList[index]
            columnStr = ""
            for i in range(len(attrList)):
                if i == len(attrList)-1:
                    columnStr = columnStr + attrList[i]
                    break
                columnStr = columnStr + attrList[i] + ","
            print(primaryKey)
            selectStr = " SELECT DISTINCT " + columnStr + " FROM " + originalName + " GROUP BY " + primaryKey + ";"
            insertStr = insertStr + selectStr
            self.cursor.execute(insertStr)
            self.connection.commit()
