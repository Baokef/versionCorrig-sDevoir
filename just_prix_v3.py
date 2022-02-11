from random import randint


print("bienvenu dans le juste prix !")
mode_facile = 1
mode_normal = 2
mode_personnalisé = 3
mode_choisi = int(input(f"veuillez choisir votre mode: {''}"))
if mode_choisi == 1:
    propostionDePrix = int(input("Veuillez entrer votre prix : "))
    justPrix = randint(1, 100)
    while True:
        if propostionDePrix < justPrix:
            print("c'est plus ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))

        elif propostionDePrix > justPrix:
            print("c'est moins ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))

        elif propostionDePrix == justPrix:
            print(justPrix)
            print(
                f"Félicitations, le juste prix était bien de {justPrix} ... ! \n")

            break
        else:
            exit()
elif mode_choisi == 2:
    essai = 10
    print(f"vous avez   {essai} essais ")
    propostionDePrix = int(input("Veuillez entrer votre prix : "))
    essai -= 1
    justPrix = randint(1, 100)
    print(f"il vous reste   {essai} essais ")
    while True and essai > 0:
        if propostionDePrix < justPrix:
            print("c'est plus ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))
            essai -= 1
            print(f"il vous reste   {essai} essais ")

        elif propostionDePrix > justPrix:
            print("c'est moins ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))
            essai -= 1
            print(f"il vous reste   {essai} essais ")

        elif propostionDePrix == justPrix:
            print(justPrix)
            print(
                f"Félicitations, le juste prix était bien de {justPrix} ... ! \n")

            print(f"vous avez réussi en  {10-essai} essais ")
            break
        else:
            exit()
elif mode_choisi == 3:
    print("bienvenu dans le juste prix !")
Prix_max = int(input(f"choisi le prix max {''}"))
nbr_essai = int(input(f"choisi le nombre d'essais {''}"))
if nbr_essai == 0:
    propostionDePrix = int(input("Veuillez entrer votre prix : "))
    justPrix = randint(1, Prix_max)
    while True:
        if propostionDePrix < justPrix:
            print("c'est plus ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))

        elif propostionDePrix > justPrix:
            print("c'est moins ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))

        elif propostionDePrix == justPrix:
            print(justPrix)
            print(
                f"Félicitations, le juste prix était bien de {justPrix} ... ! \n")

            break
        else:
            exit()
else:
    nbr_essai = nbr_essai
    print("bienvenu dans le juste prix !")
    essai = nbr_essai
    print(f"vous avez   {nbr_essai} essais ")
    propostionDePrix = int(input("Veuillez entrer votre prix : "))
    essai -= 1
    justPrix = randint(1, Prix_max)
    print(f"il vous reste   {essai} essais ")
    while True and essai > 0:
        if propostionDePrix < justPrix:
            print("c'est plus ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))
            essai -= 1
            print(f"il vous reste   {essai} essais ")

        elif propostionDePrix > justPrix:
            print("c'est moins ! \n")
            propostionDePrix = int(input("Veuillez entrer votre prix : "))
            essai -= 1
            print(f"il vous reste   {essai} essais ")

        elif propostionDePrix == justPrix:
            print(justPrix)
            print(
                f"Félicitations, le juste prix était bien de {justPrix} ... ! \n")

            print(f"vous avez réussi en  {10-essai} essais ")
            break
        else:
            exit()
