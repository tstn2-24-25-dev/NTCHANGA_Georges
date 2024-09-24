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

# magasins : stocke les produits (nom de produit et prix)
magasins = lignes[1:]
print(magasins)
dico=[]

#procuvtion : est une fonction qui creer range dans la liste dico le nom de produit suivi de leurs prix
def production():

    for produits in magasins:
        produit = produits.split(" ")
        dico.append(produit[0])
        dico.append(int(produit[1]))
        #dico_tri=sorted(dico, key=dico.get, reverse=True)
    print(dico)
    #print(dico_tri[0])
production()

#Creation d'une fonction qui permetra de calculer la sommes des artivles qui se repetent

recencement_nom = dico[0::2]

'''for nom in recencement_nom:
    index_recencement=[]
    for meme in range(recencement_nom.index(nom)):
        if(nom == meme):'''
recencement_prix=dico[1::2]
recencement={}




for i,val in enumerate(recencement_nom):
    print(i,val)





    # pas besoin de fermer le fichier: c'est fait automatiquement à la sortie du bloc "with"


