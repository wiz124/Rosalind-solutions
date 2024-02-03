f= open('rosalind_iev.txt','r')
o= open('output.txt', 'w')

# organizing input variables
param=[]
for line in f:
    for word in line.split():
            param.append(word)
#assigning input variables for algo        
one=int(param[0])
two=int(param[1])
three=int(param[2])
four=int(param[3])
five=int(param[4])
six=int(param[5])

#algo
offspring=(one*2)+(two*2)+(three*2)+(four*2)*.75+(five*2)*.5+six*0

#return solution
print(offspring)








f.close()
o.close()
