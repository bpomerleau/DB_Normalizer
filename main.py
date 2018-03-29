from Database import *
from Normaliser import *

    # Program flow:
    # (not necessarily all executed in main, I'm just trying to decrypt the assignment spec)
    #
    # -get database name from user
    # -connect to database
    #
    # - Part I: BCNF normalisation and decomposition:
    #       -show user table schemas from InputRelationSchemas
    #       -get user to select a schema from table
    #       -perform BCNF conversion on FDs (process FDs in order they are in string)
    #           - for each FD (in order), check if violates BCNF --> if it does, decompose
    #       -store resulting decomposition of schema in OutputRelationSchemas (one entry per schema, follow naming rules from assigment spec)
    #       -display to user whether or not decompostion is dependency conserving
    #       -if an instance of the original schema exists in database, implement the decomposition by
    #           creating tables for each schema and populating with data from original
    #
    #
    #
    #
    # - Part II: Compute attribute closure:
    #       - user selects one or more table entries in InputRelationSchemas
    #       - FDs are the union of all FDs from selected schemas
    #       - user selects set of attributes over which to compute closure
    #           - entered as a comma separated string
    #       - show list of attributes in closure (in alphabetical order)
    #
    #
    #
    #
    #
    #  - Part III: Equivalent Sets of FD
    #       - note* computing whether two sets are equivalent is necessary for checking dependency conserving in part I
    #       - user selects one or more table entries in InputRelationSchemas
    #       - FDs are the union of all FDs from selected schemas. This is set F1
    #       - repeat the same to get set F2
    #       - note* these steps are the same as the first steps in "Compute attribute closure"
    #       - tell the user whether the two sets are equivalent
def printTable(rows):
    # good enough for now
    for row in rows:
        print(row)

def BCNFconvert():
    print(chr(27) + "[2J")
    norm = Normaliser()
    print("Select a schema by name. Press q to quit.")
    printTable(db.getInputTable())
    while(True):
        name = input("->")
        if db.nameExists(name):   #TODO check for empty name
            print("Valid schema name.")
            norm.normalise(db, name)
            #check dependency conserving and tell user
            return
        elif name == 'q':
            return
        else:
            print("Invalid schema name. Try again.")

def AttributeClosure():
    print(chr(27) + "[2J")
    schemas = []
    FDs = ()
    printTable(db.getInputTable())
    print("")
    print("Add a schema by name. When finished press enter. q to quit.")
    while True:
        name = input("->")
        if name == "":
            break
        elif db.nameExists(name):
            if name not in schemas:
                schemas.append(name)
                print("Schema added.")
            else:
                print("Selection already included.")
        elif name == 'q':
            return
        else:
            print("Invalid name. Try again.")
    for name in schemas:
        tmp = db.getFD(name)[0] + ';'
        tmp.split(" ")
        for fd in tmp:
            FDs.append(fd)
    print(FDs)

    input("check results")

def EquivalentFDSets():
    print("Computing if two sets equivalent")

def main():
    def printMenu():
        print(chr(27) + "[2J")
        print("To perform BCNF normalisation and decompostion enter n.")
        print("To compute attribute closure enter a.")
        print("To check eqivalence between two FD sets enter e.")
        print("Press q to quit.")

    global db
    db = Database()
    printMenu()
    while(True):
        option = input("->")
        if option == 'q':
            return
        elif option == 'n':
            BCNFconvert()
            printMenu()
        elif option == 'a':
            AttributeClosure()
            printMenu()
        elif option == 'e':
            EquivalentFDSets()
            printMenu()
        else:
            print("Not a valid entry. Try again.")

if __name__ == '__main__':
    main()
