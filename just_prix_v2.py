from random import randint
print("bienvenu dans le juste prix !")
essai = 10
print(f"vous avez   {essai} essais ")
essai -= 1
propostionDePrix = int(input("Veuillez entrer votre prix : "))
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
        print(f"vous avez réussi en  {10-essai} essais ")
        print(
            f"Félicitations, le juste prix était bien de {justPrix} ... ! \n")

        break
    else:
        exit()
