#lecture du fichier des input et recolte de data ( resultat des lancee)

path = input("enter le chemin de votre fichier: ")
fichier = rf"{path}"

lignes = ""  # liste des lignes
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        hauteurs_images=ligne.split(" ")

def nombre_pages_minimum(hauteurs_images):
    pages = 1
    hauteur_restante = 10

    for image in hauteurs_images:
        hauteur = int(image)
        if  hauteur <= hauteur_restante:
            hauteur_restante -= hauteur
        else:
            pages += 1
            hauteur_restante = 10 - hauteur

    return pages


print(nombre_pages_minimum(hauteurs_images))


