class Normaliser:
    def __init__(self):
        pass

    def normalise(self, db, name):
        print("Normalising " + name)
        #normalise by BCNF
        #store new schemas in OutputRelationSchemas
        #if instances exist for 'name' create and populate tables for new schemas
