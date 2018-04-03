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
        print(tables)
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
        print("Result\n")
        for table in tables:
            print(table, "\n")
        self.encodeOutput(db,tables,name)
        #store new schemas in OutputRelationSchemas
        #if instances exist for 'name' create and populate tables for new schemas
        #check dependency conserving and tell user

    def encodeOutput(self, db, tables, name):
        for table in tables:
            sortedAttributes = sorted(table[0])
            print(sortedAttributes)
            tableName = name
            for attr in sortedAttributes:
                tableName = tableName+"_"+attr
            print(tableName)

            tableAttributes = str()
            for i in range(len(sortedAttributes)):
                if i == len(sortedAttributes)-1:
                    tableAttributes = tableAttributes + sortedAttributes[i]
                    break
                tableAttributes = tableAttributes + sortedAttributes[i] + ","
            print(tableAttributes)

            fdList = table[1]
            tableFDs = str()
            for i in range(len(fdList)):
                sortedFDLeft = sorted(fdList[i][0])
                sortedFDRight = sorted(fdList[i][1])
                leftStr = "{"
                rightStr = "{"
                for i in range(len(sortedFDLeft)):
                    if i == len(sortedFDLeft)-1:
                        leftStr = leftStr + sortedFDLeft[i] + "}"
                        break
                    leftStr = leftStr + sortedFDLeft[i] + ","

                for i in range(len(sortedFDRight)):
                    if i == len(sortedFDRight)-1:
                        rightStr = rightStr + sortedFDRight[i] + "}"
                        break
                    rightStr = rightStr + sortedFDRight[i] + ","
                tableFDs = tableFDs + leftStr + "=>" + rightStr + "; "
            print(tableFDs)
            db.outputNormalization(tableName,tableAttributes,tableFDs)
            db.addDecomposedTable(name,tableName,table)

    def decomposeAttributes(self, attrSet, fd):
        return [fd[0].union(fd[1]),attrSet.difference(fd[1].difference(fd[0]))]


    def decomposeFDs(self, attrSet, fd, fdList): #remove attributes from fds of 'remainder table' ie
        decompAttr = self.decomposeAttributes(attrSet,fd)
        returnFDs = list()
        #
        # quotientAttrSet = decompAttr[0]
        # for item in fdList:
        #     if item[0].issubset(quotientAttrSet) and item[1].intersection(quotientAttrSet):
        #         quotientfdList.append([item[0],item[1].intersection(quotientAttrSet))
        #
        # remainderAttrSet = decompAttr[1]
        # for item in fdList:
        #

        for set in decompAttr:
            partfdList = []
            for item in fdList:
                if item[0].issubset(set) and item[1].intersection(set):
                    partfdList.append([item[0],item[1].intersection(set)])
            returnFDs.append(partfdList)

        return returnFDs


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
