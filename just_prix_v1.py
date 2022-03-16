from random import randint


print("bienvenu dans le juste prix !")
propostionDePrix = int(input("Veuillez entrer votre prix : "))

justPrix = randint(1, 100)
while True:
    if propostionDePrix < justPrix:
        print("c'est pluss ! \n")
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
