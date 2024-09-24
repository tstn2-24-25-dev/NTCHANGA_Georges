def creer_grille(largeur, hauteur, rectangles):
    grille = [[0 for _ in range(largeur)] for _ in range(hauteur)]
    for x1, y1, x2, y2 in rectangles:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                grille[y][x] = 1
    return grille

def etape_suivante(grille):
    nouvelle_grille = [[0 for _ in range(len(grille[0]))] for _ in range(len(grille))]
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            voisin_haut = grille[y-1][x] if y > 0 else 0
            voisin_gauche = grille[y][x-1] if x > 0 else 0
            if voisin_haut and voisin_gauche:
                nouvelle_grille[y][x] = 1
            elif not voisin_haut and not voisin_gauche:
                nouvelle_grille[y][x] = 0
            else:
                nouvelle_grille[y][x] = grille[y][x]
    return nouvelle_grille

def compter_cellules_vivantes(grille):
    return sum(sum(ligne) for ligne in grille)

def temps_de_survie(largeur, hauteur, rectangles):
    grille = creer_grille(largeur, hauteur, rectangles)
    temps = 0
    while compter_cellules_vivantes(grille) > 0:
        grille = etape_suivante(grille)
        temps += 1
    return temps

# Lecture des données
largeur, hauteur = map(int, input().split())
n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

# Calcul et affichage du résultat
resultat = temps_de_survie(largeur, hauteur, rectangles)
print(resultat)