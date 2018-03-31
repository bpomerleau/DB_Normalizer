class Normaliser:
    def __init__(self):
        pass

    def normalise(self, db, name):
        #normalise by BCNF
            # compute closure on lhs of FD
            # if result is all attributes leave it alone
            # else decompose table
                # one table is all attributes in FD that violates BCNF
                # other table is everything less LHS of FD
        tables = []
        tables.append([db.getAttributes(name), db.getFD(name)])
        BCNF = False
        while (not BCNF)
            BCNF = True
            for table in tables:
                for fd in table[1]:
                    if not self.getClosure(self.lhs(fd), table[1]) == attr:
                    BCNF = False


                    continue
        #store new schemas in OutputRelationSchemas
        #if instances exist for 'name' create and populate tables for new schemas
        #check dependency conserving and tell user

    def equivalentSets(self, set1, set2):
        return True

    def getClosure(self, attributes, FDs):
        return attributes

    def lhs(self, fd):
        return set()
