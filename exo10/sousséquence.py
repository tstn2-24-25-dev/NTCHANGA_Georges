def est_sous_sequence(X, Y):
    i = 0  # Index pour X
    j = 0  # Index pour Y

    while i < len(X) and j < len(Y):
        if X[i] == Y[j]:
            i += 1
        j += 1

    # Si on a parcouru toute la chaîne X, c'est une sous-séquence
    return i == len(X)


# Lecture des données
X = input().strip()  # La chaîne potentielle sous-séquence
Y = input().strip()  # La chaîne principale

# Vérification et affichage du résultat
if est_sous_sequence(X, Y):
    print("OUI")
else:
    print("NON")