from collections import defaultdict
import re


def trouver_mots_frequents(textes):
    # Dictionnaire pour compter les occurrences des mots dans chaque texte
    mots_par_texte = defaultdict(set)

    # Traitement de chaque texte
    for i, texte in enumerate(textes):
        # Extraction des mots (insensible à la casse)
        mots = re.findall(r'\b[a-z]+\b', texte.lower())
        for mot in mots:
            mots_par_texte[mot].add(i)

    # Filtrer les mots qui n'apparaissent pas dans tous les textes
    n = len(textes)
    mots_filtres = {mot: len(textes) for mot, textes in mots_par_texte.items() if len(textes) < n}

    # Trier les mots par fréquence puis alphabétiquement
    mots_tries = sorted(mots_filtres.items(), key=lambda x: (-x[1], x[0]))

    # Retourner les 3 premiers mots (ou moins s'il y en a moins de 3)
    return [mot for mot, _ in mots_tries[:3]]


# Lecture des données
n = int(input())  # Nombre de textes
textes = [input() for _ in range(n)]

# Trouver les mots les plus fréquents
resultat = trouver_mots_frequents(textes)

# Afficher le résultat
for mot in resultat:
    print(mot)