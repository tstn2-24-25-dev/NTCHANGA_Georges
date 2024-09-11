fichier = r"C:\Users\IPI\Desktop\Algorithmique\exo2\exemple1.txt"

lignes = []  # future liste des lignes
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.rstrip()  # supprime la fin de ligne
        lignes.append(ligne)  # ajoute la ligne à la liste
        #print(ligne)
    #print(lignes)

#nbr_produit = int(lignes[0])
#print(nbr_produit)
magasins = lignes[1:]
print(magasins)
dico=[]

def production():

    for produits in magasins:
        produit = produits.split(" ")
        dico.append(produit[0])
        dico.append(int(produit[1]))
        #dico_tri=sorted(dico, key=dico.get, reverse=True)
    print(dico)
    #print(dico_tri[0])
production()

recencement_nom = dico[0::2]

print(recencement_nom)






    # pas besoin de fermer le fichier: c'est fait automatiquement à la sortie du bloc "with"


