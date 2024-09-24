def triRapide(tab):
    for i in range(1,len(tab)):
        j=len(tab)-i
        if (tab[i]>=tab[j]):
            tab[i],tab[j]=tab[j],tab[i]
            print(tab)

    #print(tab)
    return tab


tableau=[27,63,1,72,64,58,14,9]

triRapide(tableau)