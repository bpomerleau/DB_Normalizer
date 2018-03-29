from Database import *

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
def BCNFconvert():
    rows = db.getInputTable()
    
def AttributeClosure():
    print("Computing attribute closure")

def EquivalentFDSets():
    print("Computing if two sets equivalent")

def main():

    global db
    db = Database()
    print("To perform BCNF normalisation and decompostion enter n.")
    print("To compute attribute closure enter a.")
    print("To check eqivalence between two FD sets enter e.")
    print("Press q to quit.")
    while(True):
        option = input("->")
        if option == 'q':
            return
        elif option == 'n':
            BCNFconvert()
        elif option == 'a':
            AttributeClosure()
        elif option == 'e':
            EquivalentFDSets()
        else:
            print("Not a valid entry. Try again.")

if __name__ == '__main__':
    main()
