from Database import*

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
        # temp = temp.split(";")
    # for fd in temp:
    #     t = fd.split("=>")
    #     lst.append(t)
    print(lst)

if __name__ == "__main__":
    main()
