f= open('rosalind_iprb.txt','r')
o= open('output.txt', 'w')

#reads input to get parameters
#k=number of AA organisms
#m= number of Aa organisms
#n= number of aa organisms
#chance of two randomly selected organisms has dominant phenotype(AA or Aa)

param=[]
for line in f:
    #.split() turns string into a list of words
    for word in line.split():
        param.append(word)

k=int(param[0])
m=int(param[1])
n=int(param[2])
population=k+m+n

#formula: get chance of recessive phenotype then subtract from one
#tree formula and punette squares
'''

        P(n)   --100%aa
       /
    P(n)-P(m)  --50%aa
   /   \
  /     P(k)   --0%aa
 /     P(m)    --25%aa
/     /
---P(m)-P(n)   --50%aa
\     \
 \     P(k)    --0%aa
  \     P(m)   --0%aa
   \   /
    P(k)-P(k)  --0%aa
       \
        P(n)   --0%aa

   A | a
---------
A| AA| Aa
---------
a| Aa| aa
       
'''

chance=1-(((n**2)-n)+m*n+m*(m-1)*.25)/(population*(population-1))


print(k)
print(m)
print(n)
print(chance)

f.close()
o.close()
