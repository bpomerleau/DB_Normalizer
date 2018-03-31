
def main():
    x = ["once", "twice", "twice", "thrice"]
    y = set()
    for thing in x:
        print(thing)
        y.add(thing)
    print(y)

if __name__ == "__main__":
    main()
