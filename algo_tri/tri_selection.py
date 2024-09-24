def indiceMin(tab, j):

    min_index = j
    for i in range(j + 1, len(tab)):
        if tab[i] < tab[min_index]:
            min_index = i
    return min_index


def triSelection(tab):

    for i in range(len(tab) - 1):
        min_idx = indiceMin(tab, i)
        if min_idx != i:
            tab[i], tab[min_idx] = tab[min_idx], tab[i]
    return tab



if __name__ == "__main__":
    mon_tableau = [64, 34, 25, 12, 22, 11, 90]
    print(indiceMin(mon_tableau, 3))

    tableau_trie = triSelection(mon_tableau)
    print(tableau_trie)