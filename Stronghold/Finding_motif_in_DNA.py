from __future__ import print_function
f= open('rosalind_subs.txt','rt')
o= open('output.txt', 'w')


dna=''
motif=''
n=0
strand=[]
for line in f:
    if len(line)>len(dna):
        dna=line
    else:
        motif=line
    
#cleans up input
for word in motif.split():
    motif=word
for word in dna.split():
    dna=word



for index in range(0,len(dna)-len(motif)):
    
    n=index+len(motif)#<---for some reason the dna[] needs to take n
    
    #compare dna segment to motif
    if dna[index:n]==motif:
       
        #stores motif location to array
        strand.append(index+1)

for element in strand:
    # \n starts a new line 
    o.write(str(element)+'\n')
    


f.close()
o.close()
