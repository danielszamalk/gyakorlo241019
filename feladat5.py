def beolvas(szoveg):
    szam=int(input(szoveg))
    return szam
def ot():
    szam=beolvas("Kérem adjon meg egy 40 ás 95 közötti számot!")
    if (szam>95) or (szam<40):
        print("HIBA! Nem megfelelő szám!")
    else:
        szam=str(szam)
        print(szam[0])
#másik megoldás
        szam=int(szam)
        print(str(int(szam / 10)))


#print(str(math.floor(szam/10))) szam=int(szam) importálni kell a matekot