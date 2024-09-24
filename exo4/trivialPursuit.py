
#lecture du fichier des input et recolte de data ( resultat des lancee)

path = input("enter le chemin de votre fichier: ")
fichier = rf"{path}"

lignes = []  # liste des lignes
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        liste_intermediaire=ligne.split(" ")
    for ligne in liste_intermediaire:
        lignes.append(int(ligne))

#----------------------------------------------------------

# ordre des couleurs des cases

couleurs=["violet","orange","jaune","vert","rose","bleu"]


def retour_couleur_arrive(tableau_entier):
    position=0
    #On determine la position a l'issue de des lances en faisant la sommes des resultats des lances

    position=sum(tableau_entier)

    #pour gerer les tours complets possibles du cercle
    position_final=position%48

    #vue que nous avons une boucle de 6 couleurs nous devons a chaque fois savoir a quoi celle ci corespondes lorsque la position est grande pour cela on utilise le modulo

    position_coleur=position_final%6

    return couleurs[position_coleur]



print(retour_couleur_arrive(lignes))




