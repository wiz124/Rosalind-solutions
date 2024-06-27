import math
from itertools import permutations

#calc total permutations
def factorial(n):
    return math.factorial(n)
    
#compute all permutations
def allperm(n):
    if n==1:
        return 1
    else:
        return list(permutations(range(1,n+1)))
        
#format and output results
def output(perm,total):

        with open('output.txt','w') as f:
            
            f.write(str(total))
            
            if perm==1:
                f.write(1)
            else: 
                line =''
                for row in range(0,len(perm)):
                    for column in range(0,len(perm[row])):
                        line=line+str(perm[row][column])+' '
                    
                    f.write('\n'+line)
                    line=''
    
with open('rosalind_perm.txt','r') as f:
    for line in f:
        n=int(line)

output(allperm(n),factorial(n))
    
