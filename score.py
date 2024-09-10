data = "a 1 b 3 c 3 d 2 e 1 f 4 g 2 u 1"
t = data.split(" ")
print(t)

mot="cafe"
m = mot.split()
print(m)

dic={}

print()

#Creation de la fonction "score_mot" : elle donne le score d'un mot

def score_mot(phrase):
    #operation = '0'
    point = 0
    for i in range(len(phrase)):
      if(phrase[i] in t):
        position= t.index(phrase[i])
        #print(position)
        #operation += " + " + t[position+1]
        point += int(t[position+1])
    dic[phrase] = operation + "=" + str(point)
    print(dic)

    return point
       
score_mot("cafe")



#Creation de la fonction qui classe les elments en fonction de leurs score issus de la fonction precedent et affichage dans l'ordre
  


