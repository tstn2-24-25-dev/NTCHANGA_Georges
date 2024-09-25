T=[]
def fusinner(tab1,tab2):
        for i  in range(len(tab1)):
                j=i
                while(j<len(tab2)):
                        if(tab1[i]>tab2[j]):
                                T.append(tab1[i])
                                j=len(tab2)+1
                        else:
                                T.append(tab2[j])
                                j+=1



tab1=[8,27,33]
tab2=[14,16,31,54]

fusinner(tab1,tab2)


print(T)