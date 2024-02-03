from __future__ import print_function
f= open('rosalind_fib (1).txt','r')
o= open('output.txt', 'w')

#param is array[n,k]
#n=months
#k=population of rabbit pairs
#rules:
    #rabbits mature in one month
    #rabbits never die
    #mature rabbits produce k pairs
    #if k=1, follows fibonacci sequence
param=[]
for line in f:
    for word in line.split():#<---gets parameters 
            param.append(word)
            
n=int(param[0])
k=int(param[1])

#generation population before the previous one
holder=0
#previous generation population
prevgen=1
#current gen population
curgen=0

while n-1>0:
    #formula for current gen population
    curgen=holder*k+prevgen

    #assign values for next gen calcs
    holder=prevgen
    prevgen=curgen

    n-=1
    
print(curgen)
f.close()
o.close()
