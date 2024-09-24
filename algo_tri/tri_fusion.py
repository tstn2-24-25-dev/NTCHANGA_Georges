tableau_tri=[]
def fusionner(tab1, tab2) :
    for i in range(len(tab1)) :
        if(tab1[i] < tab2[i]):
            tableau_tri.append(tab2[i])
        else:
            if(tab1[i]>tab2[i+1]):
                tableau_tri.append(tab2[i])


