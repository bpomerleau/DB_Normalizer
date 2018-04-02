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
        table = [db.getAttributeSet(name), db.getFDSetList(name)]
        BCNF = False
        while not BCNF:
            BCNF = True
            for fd in table[1]:
                if not self.getClosure(fd).issubset(table[0]):
                    BCNF = False


                    continue
        #store new schemas in OutputRelationSchemas
        #if instances exist for 'name' create and populate tables for new schemas
        #check dependency conserving and tell user

    def equivalentSets(self, set1, set2):
        return True

    def getClosure(self, fd):

        return fd[0]

    def lhs(self, fd):
        return fd[0]
