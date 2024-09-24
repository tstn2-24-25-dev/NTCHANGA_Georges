def puissance_apres_4_mois(puissance_initiale):
    puissance = puissance_initiale

    for _ in range(4):  # Répéter 4 fois pour simuler 4 mois
        if puissance % 3 == 0:
            puissance //= 3
        elif puissance % 2 == 0:
            puissance //= 2
        else:
            puissance -= 1

    return puissance


# Fonction pour tester plusieurs cas
def tester_puissances(puissances):
    for puissance in puissances:
        resultat = puissance_apres_4_mois(puissance)
        print(f"Puissance initiale : {puissance}, Puissance après 4 mois : {resultat}")


# Test du programme
puissances_test = [10, 25, 100, 64, 81]
tester_puissances(puissances_test)