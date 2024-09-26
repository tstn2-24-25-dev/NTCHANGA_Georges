
def fusinner(tab1,tab2):
        T=[]
        for i  in range(len(tab1)):
                max_tab1= max(tab1)
                max_tab2= max(tab2)
                if(max_tab1>max_tab2):
                        a=tab1.index(max_tab1)
                else:
                        a=tab2.index(max_tab2)
                j=i
                while(j<len(tab2)):
                        if(tab1[i]<tab2[j]):
                                T.append(tab1[i])
                                j=len(tab2)+1
                        else:
                                T.append(tab2[j])
                                a=j
                                j+=1
                #T.extend(tab1[i:])
        T.extend(tab2[a:])
        return T


def tri_fusion(tab):
        #division de la table en deux
        n = len(tab)//2
        tab1=tab[:n]
        tb2=tab[n:]
        #utilisation de la recurcivite
        tab1=tri_fusion(tab1)
        tb2=tri_fusion(tb2)
        #Appel de la fonction fusionner
        fusinner(tab1,tb2)







