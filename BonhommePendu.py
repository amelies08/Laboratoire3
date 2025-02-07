reponse1 = "w" #variables des reponses
reponse2 = "h"
reponse3 = "a"
reponse4 = "m"

lettre1 = lettre2 = lettre3 = lettre4 = "_" #variables pour montrer le nombre de lettres et l'emplacement des lettres

bonhomme1 = "o"
bonhomme2 = "|"
bonhomme3 = "^"

print("Devine le groupe de musique")
mauvais = 0 #mauvaises reponses
guess = input()

while (lettre1 != reponse1 or lettre2 != reponse2 or lettre3 != reponse3 or lettre4 != reponse4) and mauvais < 3: #pendant qu'il y a au moins un lettre qui n'est pas devine et qu'il y a moins de 3 mauvaises reponses
    print("Nombre de mauvaises reponses:", mauvais)
    if guess == reponse1: #changer la ligne de la bonne reponse pour que la lettre et son emplacement soient indiques
        lettre1 = "w"
        print("bonne reponse")
    elif guess == reponse2:
        lettre2 = "h"
        print("bonne reponse")
    elif guess == reponse3:
        lettre3 = "a"
        print("bonne reponse")
    elif guess == reponse4:
        lettre4 = "m"
        print("bonne reponse")
    else:
        mauvais = mauvais + 1 #changer le nombre de mauvaises reponse lorsque necessaire et inscrire ce nombre
        print("mauvaise reponse")
        if mauvais == 1:
            print(bonhomme1) #Ajouter une partie du bonhomme
        else:
            print(bonhomme1)
            print(bonhomme2)
    print(lettre1, lettre2, lettre3, lettre4) #ecrire les lettres devoilees et leur emplacements
    guess = input() #deviner une autre lettre
else: #s'il y a 3 mauvaises reponses ou que toutes les reponses sont bonnes
    if lettre1 == reponse1 and lettre2 == reponse2 and lettre3 == reponse3 and lettre4 == reponse4 and mauvais < 3: #si toutes les lettres sont devoilees et qu'il y a moins de 3 mauvaises reponses
        print("bravo")
    elif mauvais == 3: #s'il y a 3 mauvaises reponses
        print(bonhomme1)
        print(bonhomme2)
        print(bonhomme3)
        print("game over")