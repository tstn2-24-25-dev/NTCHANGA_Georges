def derniere_delegation(distances, vitesses):
    n = len(distances)  # Nombre de délégations
    temps_arrivee = []  # Liste pour stocker les temps d'arrivée

    # Calcul du temps d'arrivée pour chaque délégation
    for i in range(n):
        temps = distances[i] / vitesses[i]
        temps_arrivee.append((temps, i))  # On stocke le temps et l'index de la délégation

    # Tri des délégations par temps d'arrivée (du plus long au plus court)
    temps_arrivee.sort(reverse=True)

    # La délégation qui arrive en dernier est la première de la liste triée
    derniere = temps_arrivee[0][1]

    return derniere + 1  # On ajoute 1 car les indices commencent à 0


