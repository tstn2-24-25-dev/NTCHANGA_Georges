def triInsertion(tab):
    #m_idx=0
    for i in  range(1,len(tab)):
        for j in range(i):
            if(tab[i] < tab[j]):
                tab[j],tab[i]=tab[i],tab[j]
    print(tab)
    return tab



if __name__ == '__main__':
    tableau = [4, 8, 2, 10, 1, 9, 7, 6, 3, 5]


    triInsertion(tableau)

