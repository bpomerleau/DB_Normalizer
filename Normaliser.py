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
                    # print("FD",fd,"\n")
                    # print("Closure",self.getClosure(fd[0],table[1]),"\n")
                    # print("Attributes",table[0],"\n")
                    if not (self.getClosure(fd[0], table[1]) >= table[0]):
                        BCNF = False
                        # print("FD attr ",fd[0],"\n")
                        # print("FD R",fd[1],"\n")
                        decompFD = self.decomposeFDs(table[0],fd,table[1])
                        decompAttr = self.decomposeAttributes(table[0],fd)

                        table1 = [decompAttr[0],decompFD[0]]
                        # print("TABLE ",table[0],"\n")
                        table2 = [decompAttr[1],decompFD[1]]
                        tables.remove(table)
                        tables.append(table1)
                        tables.append(table2)
                        break
                break
        print("Result\n")
        for table in tables:
            print(table, "\n")
        #store new schemas in OutputRelationSchemas
        #if instances exist for 'name' create and populate tables for new schemas
        #check dependency conserving and tell user

    # def ouputNormalization(self, db, tables):


    def decomposeAttributes(self, attrSet, fd):
        return [fd[0].union(fd[1]),attrSet.difference(fd[1].difference(fd[0]))]


    def decomposeFDs(self, attrSet, fd, fdList): #remove attributes from fds of 'remainder table' ie
        decompAttr = self.decomposeAttributes(attrSet,fd)
        quotientfdList = list()
        remainderfdList = list()

        quotientAttrSet = decompAttr[0]
        for item in fdList:
            if item[0] <= quotientAttrSet:
                # print(item)
                quotientfdList.append(item)

        remainderAttrSet = decompAttr[1]
        # print("Remainder Set",remainderAttrSet,"\n")
        for item in fdList:
            if item[0] <= remainderAttrSet:
                temp = item[1].difference(attrSet.difference(remainderAttrSet))
                if temp:
                    remainderfdList.append([item[0],temp])

        return [quotientfdList,remainderfdList]


    def equivalentSets(self, set1, set2):
        return True

    def getClosure(self, attr, fds):
        closure = attr #SET of lhs attributes
        old = set()
        while old != closure:
            old = closure
            for fd in fds:
                if fd[0].issubset(closure) and not fd[1].issubset(closure):
                    closure = closure.union(fd[1])
        return closure

    def lhs(self, fd):
        return fd[0]
