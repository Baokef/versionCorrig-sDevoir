from random import randint


print("bienvenu dans le juste prix !")
mode_facile = 1
mode_normal = 2
mode_personnalise = 3
mode_choisi = int(input(f"veuillez choisir votre mode: {''}"))
if mode_choisi == 1:
    proposition_de_prix = int(input("Veuillez entrer votre prix : "))
    juste_prix = randint(1, 100)

    while True:
        if proposition_de_prix < juste_prix:
            print("c'est moins ! \n")
            proposition_de_prix = int(input("Veuillez entrer votre prix : "))

        elif proposition_de_prix > juste_prix:
            print("c'est plus ! \n")
            proposition_de_prix = int(input("Veuillez entrer votre prix : "))

        elif proposition_de_prix == juste_prix:
            print("Félicitations...! \n")
            print(juste_prix)
            break
        else:
            exit()
elif mode_choisi == 2:
    essai = 10
    print(f"vous avez   {essai} essais ")
    juste_prix = randint(1, 100)
    print(juste_prix)
    proposition_de_prix = int(input("Veuillez entrer votre prix : "))
    essai -= 1
    print(f"il vous reste   {essai} essais ")
    while True and essai >= 0:
        if proposition_de_prix < juste_prix:
            print("c'est moins ! \n")
            proposition_de_prix = int(input("Veuillez entrer votre prix : "))
            essai -= 1
            print(f"il vous reste   {essai} essais ")
            if essai == 0:
                print("le juste prix etait de : ", juste_prix)

        elif proposition_de_prix > juste_prix:
            print("c'est plus ! \n")
            proposition_de_prix = int(input("Veuillez entrer votre prix : "))
            essai -= 1
            print(f"il vous reste   {essai} essais ")
            if essai == 0:
                print("le juste prix etait de : ", juste_prix)
                break
        elif proposition_de_prix == juste_prix:
            print("Félicitations...! \n")
            print(juste_prix)
            print(f"vous avez réussi en  {10-essai} essais ")
            break
        else:
            exit()
elif mode_choisi == 3:
    print("bienvenu dans le juste prix !")
    Prix_max = int(input(f"Veuillez choisir le prix max {''}"))
    nbr_essai = int(input(f"Veuillez choisir le nombre d'essais {''}"))
    if nbr_essai == 0:
        proposition_de_prix = int(input("Veuillez entrer votre prix : "))
        juste_prix = randint(1, Prix_max)
        while True:
            if proposition_de_prix < juste_prix:
                print("c'est moins ! \n")
                if essai == 0:
                    print("le juste prix etait de : ", juste_prix)
                proposition_de_prix = int(
                    input("Veuillez entrer votre prix : "))

            elif proposition_de_prix > juste_prix:
                print("c'est plus ! \n")
                if essai == 0:
                    print("le juste prix etait de : ", juste_prix)
                proposition_de_prix = int(
                    input("Veuillez entrer votre prix : "))

            elif proposition_de_prix == juste_prix:
                print("Félicitations...! \n")
                print(juste_prix)

                break
            else:
                exit()
    else:
        nbr_essai = nbr_essai
        print("bienvenu dans le juste prix !")
        essai = nbr_essai
        print(f"vous avez   {nbr_essai} essais ")
        proposition_de_prix = int(input("Veuillez entrer votre prix : "))
        essai -= 1
        juste_prix = randint(1, Prix_max)
        print(f"il vous reste   {essai} essais ")
        while True and essai > 0:
            if proposition_de_prix < juste_prix:
                print("c'est moins ! \n")
                proposition_de_prix = int(
                    input("Veuillez entrer votre prix : "))
                essai -= 1
                print(f"il vous reste   {essai} essais ")
                if essai == 0:
                    print("le juste prix etait de : ", juste_prix)
            elif proposition_de_prix > juste_prix:
                print("c'est plus ! \n")
                proposition_de_prix = int(
                    input("Veuillez entrer votre prix : "))
                essai -= 1
                print(f"il vous reste   {essai} essais ")
                if essai == 0:
                    print("le juste prix etait de : ", juste_prix)
            elif proposition_de_prix == juste_prix:
                print("Félicitations...! \n")
                print(juste_prix)
                print(f"vous avez réussi en  {10-essai} essais ")
                break
            else:
                exit()
