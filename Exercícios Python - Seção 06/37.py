for i in range(1000, 10000):
    n1 = int(i.__str__()[0:2])
    n2 = int(i.__str__()[2:4])
    if (n1 + n2)**2 == i:
        print(i)
