aukera = 0

print("MENUA")
print("1.Hilabeteak")
print("2.Faktoriala")
print("3.Zenbaki handiena")
print("4.Laukizuzena marraztu")
print("5.Triangelua marraztu")
print("6.Erronboa marraztu")
print("7.Irten")
while int(aukera) != 7:
    aukera = input("Aukeratu zerbait: ")
    print("")

    if int(aukera) == 1:
        from egunak import hilabetearenIzena
        hilabetearenIzena()
    elif int(aukera) == 2:
        from eragiketak import faktoriala
        faktoriala()
    elif int(aukera) == 3:
        from eragiketak import handiena
        handiena()
    elif int(aukera) == 4:
        from irudiak import laukizuzena
        laukizuzena()
    elif int(aukera) == 5:
        from irudiak import triangelua
        triangelua()
    elif int(aukera) == 6:
        from irudiak import erronboa
        erronboa()
