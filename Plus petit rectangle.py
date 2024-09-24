def trouver_rectangle_englobant(rectangles):
    # Initialiser les valeurs min et max avec le premier rectangle
    x_min, y_min = float('inf'), float('inf')
    x_max, y_max = float('-inf'), float('-inf')

    for rectangle in rectangles:
        # Extraire les coordonnées de chaque rectangle
        x1, y1, x2, y2 = map(int, rectangle.split())

        # Mettre à jour les valeurs min et max
        x_min = min(x_min, x1, x2)
        y_min = min(y_min, y1, y2)
        x_max = max(x_max, x1, x2)
        y_max = max(y_max, y1, y2)

    # Retourner les coordonnées du rectangle englobant dans l'ordre demandé
    return [
        (x_min, y_min),
        (x_min, y_max),
        (x_max, y_min),
        (x_max, y_max)
    ]

# Lecture des données
n = int(input())  # Nombre de rectangles
rectangles = [input() for _ in range(n)]

# Trouver le rectangle englobant
resultat = trouver_rectangle_englobant(rectangles)

# Afficher le résultat
for coord in resultat:
    print(f"{coord[0]} {coord[1]}")