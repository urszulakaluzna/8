import random


c = 3
while(c > 0):
    a = int(input("Papier = 1, kamień = 2 czy nożyce = 3 ?\n "))
    b = random.randrange(1, 3)

    if a == 1 and b == 1:
        print("Remis. \nSpróbuj jeszcze raz.")
        c-=1
    elif a == 1 and b == 2:
        print("Papier bije kamień! Wygrałeś!!! \nSpróbuj jeszcze raz.")
        c-=1
    elif a == 1 and b == 3:
        print("Nożyce tną papier. Przegrałeś! \nSpróbuj jeszcze raz.")
        c-=1
    elif a == 2 and b == 1:
        print("Papier bije kamień! Przegrałeś! \nSpróbuj jeszcze raz.")
        c -= 1
    elif a == 2 and b == 2:
        print("Remis. \nSpróbuj jeszcze raz.")
        c -= 1
    elif a == 2 and b == 3:
        print("Kamień niszczy nożyce! Wygrałeś!!! \nSpróbuj jeszcze raz.")
        c -= 1
    elif a == 3 and b == 1:
        print("Nożyce tną papier! Wygrałeś!!! \nSpróbuj jeszcze raz.")
        c -= 1
    elif a == 3 and b == 2:
        print("Kamień niszczy nożyce! Przegrałeś!!! \nSpróbuj jeszcze raz.")
        c -= 1
    elif a == 3 and b ==3:
        print("Remis. \nSpróbuj jeszcze raz.")
        c -= 1
