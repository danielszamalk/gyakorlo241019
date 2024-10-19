def negy():
    k=1
    n=1
    if (k%2==1) and (n>0) and (pow(2,n)>k):
        print("Proth számok: ", end="")
        for n in range(0, 9, 1):
            proth = (k * pow(2, n)) + 1
            print(str(proth) + ", ", end="")
        proth = (k * pow(2, 10)) + 1
        print(proth)
    else:
        print("HIBA: Nem megfelelő számok!")

def negyb():
    k = 1
    n = 1
    print("Proth számok: ", end="")
    while n>10:
        if (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
            proth = (k * pow(2, n)) + 1
            print(str(proth) + ", ", end="")
            n+=1
        else:
            print("HIBA: Nem megfelelő számok!")
    proth = (k * pow(2, 10)) + 1
    print(proth)
