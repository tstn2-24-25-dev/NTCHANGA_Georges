T=[]
def fusinner(tab1,tab2):
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


tab1=[8,27,33]
tab2=[14,16,31,54]

fusinner(tab1,tab2)


print(T)