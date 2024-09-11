#Gestion du fichier des data
path = input("enter le chemin de votre fichier: ")
fichier = rf"{path}"

lignes = []  # liste des lignes
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.rstrip()  # supprime la fin de ligne
        lignes.append(ligne)  # ajoute la ligne à la liste




#creation de la liste / chaine de charactere contenant les associtions des lettres  aux points

data = lignes[0]
print(data)
t = data.split(" ")
print(t)

#creation de la variable phrases : c'est la liste issues des mots à testés



#Creation du dictionnaire dic qui contiendra les mots (key) et leurs scores (values)

dic={}

#Creation de la fonction "score_mot" : elle donne le score d'un mot

def score_mot(mots):
    #score = 0
    point = 0
    for i in range(len(mots)):
      if(mots[i] in data):
        position= t.index(mots[i])
        point += float(t[position+1])
    dic[mots] = point

    return dic

# Creation de la fonction parcourt_ phrase : elle parcourt une phrase(liste) et applique la fonction score_mot à chaque mot de cette phrase
def parcourt_phrase(phrases):
    for phrase in phrases:
        score_mot(phrase)
    sorted(dic)
    print(dic)
    return dic


#Affichage à la sortie

phrases = ["cafe","face","bad","bug","zebra","button"]

parcourt_phrase(phrases)







  


