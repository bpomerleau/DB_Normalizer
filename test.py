from Database import*
from Normaliser import*

def main():
    x = ["once", "twice", "twice", "thrice"]
    y = set()
    for thing in x:
        print(thing)
        y.add(thing)
    print(y)
    #Experimenting with parsing the database output into something useful for calculating closure
    db = Database()
    fds = db.getFD("Person")
    lst = list()
    for fd in fds:
        temp = fd.replace("{","")
        temp = temp.replace("}","")
        temp = temp.replace(";","")
        lst.append(temp.split("=>"))
    for fd in lst:
        fd[0] = set(fd[0].split(","))
        fd[1] = set(fd[1].split(","))
    #lst is now a list of two element lists containing the sets of each side of the =>
    #making them lists of sets makes it easy to do subset checks for the closure calculation
    print(lst)
    attrList = db.getAttributes("Person").split(",")
    print(set(attrList))
    norm = Normaliser()
    norm.normalise(db,"Person")

if __name__ == "__main__":
    main()
