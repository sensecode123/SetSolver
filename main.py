while True:
    a = int(input("How manny in the set: "))
    b = int(input("Set 1: "))
    c = int(input("Set 2: "))
    d = int(input("Non of the sets: "))
    e = int(input("Intersection: "))

    if e > 0:

        print("Intersection: ")
        print(e)
        print("")

        print("Sets only: ")
        print("set1 :")

        print(b - e)

        print("")

        print("set2: ")
        print(c - e)

        print("")

        print("Non of the sets: ")
        print(d)

    if e == 0:
        print("Intersection: ")

        g = b - e + e + c - e + d

        s = g - a

        print(s)

        print("Sets only: ")
        print("set1: ")

        print(b - s)

        print("")

        print("set2: ")
        print(c - s)

        print("")

        print("Non of the sets: ")
        print(d)