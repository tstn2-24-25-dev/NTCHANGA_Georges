def indicemin(tab:list,j:int)->int:
    min_tab = tab[j]
    for i in range(j,len(tab)-1):
        min_tab = min(tab[i],tab[i+1])
    print(tab.index(min_tab))
    return tab.index(min_tab)

def triSelection(tableau:list)->list:
    for i in range(len(tableau)):
        a=indicemin(tableau,tableau[i])
        print(a)
        b=tableau[i]
        tableau[i]=tableau[a]
        tableau[a]=b
        print(tableau)
    return tableau


tableau=[4,6,5,2,1,0,3]
tableau1=[7,2,11,5]

indicemin(tableau1,0)

#triSelection(tableau)