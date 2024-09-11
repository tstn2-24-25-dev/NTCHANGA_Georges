#gestions de fichiers (ouverture et stackage de variables)

path = input("enter le chemin de votre fichier: ")
fichier = rf"{path}"

lignes = []  # liste des lignes
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.rstrip()  # supprime la fin de ligne
        lignes.append(ligne)  # ajoute la ligne à la liste


p = int(lignes[0])

# on accede aux elments de la lignes a parti du 3eme element  puis on compares les valeurs a la moitier ie P/2
for requets in lignes[2::]:
    requet = requets.split(" ")
    if (int(requet[1]) >= p/2):
        print(requet[0])
