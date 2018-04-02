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
        tables = [[db.getAttributeSet(name), db.getFDSetList(name)]]
        BCNF = False
        while not BCNF:
            BCNF = True
            for table in tables:
                for fd in table[1]:
                    if not self.getClosure(fd[0], table[1]) >= table[0]:
                        BCNF = False
                        fds1 = [fd]
                        table1 = [fd[0].union(fd[1]),fds1]

                        continue
        #store new schemas in OutputRelationSchemas
        #if instances exist for 'name' create and populate tables for new schemas
        #check dependency conserving and tell user

    def decomposeFDs(self, fd, fdList): #remove attributes from fds of 'remainder table' ie
        newfdList = fdList.remove(fd)   #given ABCD:{A->ABCD,B->C} decompose into AD:{A->D} and BC:{B->C} where the former is remainder
        attrSet = fd[0].union(fd[1])    #this function currently only decomposes the FD list
        for item in newfdList:
            temp = item[0]|attrSet
            if temp:
                for attr in temp:
                    item[0].remove(attr)
            temp = item[1]|attrSet:
            if temp:
                for attr in temp:
                    item[1].remove(attr)
            if not item[0] and not item[1]:
                newfdList.remove(item)
        return newfdList

    def equivalentSets(self, set1, set2):
        return True

    def getClosure(self, attr, fds):
        closure = attr #SET of attributes
        old = set()
        while old != closure:
            old = closure
            for fd in fds:
                if fd[0].issubset(closure) and not fd[1].issubset(closure):
                    closure = closure.union(fd[1])
        return closure

    def lhs(self, fd):
        return fd[0]
