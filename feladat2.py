def ketto():
    szam=int(input("Kérem adjon meg egy öttel osztható háromjegyű számot!"))
    negyzet=szam**2
    if (((szam>99) and (szam<1000)) or ((szam<-99)and (szam>-1000))) and szam%5==0:
        print(negyzet)
    else:
        print("Nem megfelelő szám!")