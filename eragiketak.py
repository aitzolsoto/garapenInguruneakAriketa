lista1 = [20,10,3000,4502,2222,10532,1];

def faktoriala():
    zenbakia = input("Sartu zenbaki bat: ")
    emaitza = 1
    while int (zenbakia) > 0:
        emaitza = int(emaitza) * int (zenbakia)
        zenbakia = int (zenbakia) - 1

    print(emaitza)

def handiena():
    print(max(lista1))

