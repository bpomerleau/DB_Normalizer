import sqlite3

class Database():

    def __init__(self):
        # get user input for self.__dbpath
        print(chr(27) + "[2J")
        self.__dbpath = input("Enter name of database file: ")
        self.connection = sqlite3.connect(self.__dbpath)
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(' PRAGMA foreign_keys = ON; ')
        self.connection.commit()
        print("Connected to database.")

    def getInputTable(self):
        pass
