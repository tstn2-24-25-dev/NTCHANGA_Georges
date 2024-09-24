import math


def evaluer_expression(tokens):
    if len(tokens) == 1:
        return int(tokens[0])

    operateur = tokens[0]
    if operateur in ['+', '-', '*', '/']:
        # Trouver la position qui sépare les deux sous-expressions
        position_separation = 1
        profondeur = 0
        for i, token in enumerate(tokens[1:], 1):
            if token in ['+', '-', '*', '/']:
                profondeur += 1
            elif token.isdigit():
                if profondeur == 0:
                    position_separation = i + 1
                    break
                profondeur -= 1

        gauche = evaluer_expression(tokens[1:position_separation])
        droite = evaluer_expression(tokens[position_separation:])

        if operateur == '+':
            return gauche + droite
        elif operateur == '-':
            return gauche - droite
        elif operateur == '*':
            return gauche * droite
        elif operateur == '/':
            return math.floor(gauche / droite)  # Division entière arrondie vers le bas
    else:
        return int(operateur)


# Lecture de l'expression
expression = input().split()

# Évaluation et affichage du résultat
resultat = evaluer_expression(expression)
print(resultat)