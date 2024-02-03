f= open('rosalind_cons (3).txt','r')
o= open('output.txt', 'w')

dna=[]
dnastring=[]
inputs={}
tag=''
string=''

#read input file
#turns input into dictionary format, easier to access
for line in f:
    if '>' in line:
        inputs.update({line:''})
        tag=line
    else:
        inputs.update({tag:str(inputs[tag]+line).strip()})
#take dictionary and transform it into 2d matrix
for key,value in dict.items(inputs):
    for word in value:
        dna.append(word)
    dnastring.append(dna)
    dna=[]


A=[]
G=[]
C=[]
T=[]
acount=0
gcount=0
ccount=0
tcount=0

#profile
#iterate down each column 
for column in range(0,len(dnastring[0])):
    for row in range(0,len(dnastring)):

        #counts each base pair in the column
        if dnastring[row][column]=='A':
            acount+=1
            
        if dnastring[row][column]=='G':
            gcount+=1
           
        if dnastring[row][column]=='C':
            ccount+=1
            
        if dnastring[row][column]=='T':
            tcount+=1
            
    #addes counts to an array for storage         
    A.append(acount)
    G.append(gcount)
    C.append(ccount)
    T.append(tcount)
    
    #reset counts for next column
    acount=0
    gcount=0
    ccount=0
    tcount=0

'''
2d array coordinate positions
[row pos][column pos]
    1     2     3     4  
1 (1,1) (1,2) (1,3) (1,4)
2
3
4
'''

consensus=''
#consensus
for position in range(0,len(A)):
    if A[position]==max(A[position],G[position],C[position],T[position]):
        consensus=consensus+'A'
        #elif statement for logic control 
    elif C[position]==max(A[position],G[position],C[position],T[position]):
        consensus=consensus+'C'
    elif G[position]==max(A[position],G[position],C[position],T[position]):
        consensus=consensus+'G'
    elif T[position]==max(A[position],G[position],C[position],T[position]):
        consensus=consensus+'T'

#outputting to file
o.write(consensus +'\n')
o.write('A: ')
for element in A:
    o.write(str(element)+' ')
    
o.write('\n'+'C: ')
for element in C:
    o.write(str(element)+' ')
    
o.write('\n'+'G: ')
for element in G:
    o.write(str(element)+' ')

o.write('\n'+'T: ')
for element in T:
    o.write(str(element)+' ')
    


f.close()
o.close()
               
    
