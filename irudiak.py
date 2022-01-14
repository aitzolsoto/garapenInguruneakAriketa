def laukizuzena():
    zabalera = input("Sartu zabalera: ")
    altuera = input("Sartu altuera: ")
    for i in range(int(altuera)):
        for j in range(int(zabalera)):
            print("*", end="")
        print("")


def triangelua():
    zabalera = input("Sartu zabalera: ")
    for i in range(int(zabalera)):
        for j in range(int(zabalera)):
            if i + j >= int(zabalera) :
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(int(zabalera)):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

def erronboa():
    zabalera = input("Sartu zabalera: ")
    for i in range(int(zabalera)):
        for j in range(int(zabalera)):
            if i + j >= int(zabalera) :
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(int(zabalera)):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

    for i in range(int(zabalera)):
        for j in range(int(zabalera)):
            if j > i:
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(int(zabalera)):
            if j + i < int(zabalera):
                print("*", end="")
            else:
                print(" ", end="")
        print("")



