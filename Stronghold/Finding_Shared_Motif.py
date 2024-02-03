# code WIP
f= open('rosalind_lcsm.txt','r')
o= open('output.txt', 'w')

#finds a matching substring to the entry substring
def motiffinder(n,motif):
   hit=''
   #traverse through dictionary, finds substring in DNA string
   #return None if substring not there
   for key,value in dict.items(n):
       if motif in value:
            hit=motif
            return hit
       else:
           return None
        
#converts database into key/value pair
Dnadata={}
string=''
for line in f:
    #identifies if line is id line
    if '>' in line:
        line=line.strip()
        Dnadata.update({line:''})
        string=line
    #identifies dna strand, also concatenates
    #stores it to appropriate fasta id
    else:
        Dnadata.update({string:str(Dnadata[string]+line).strip()})


#goes through dictionary and takes all possible substrings in an entry.
#only takes all substrings from one dictionary entry 
hit=[]
suspect=''
motif=''
i=0
finderdict={}
for key, value in dict.items(Dnadata):
    #create a separate copy of Dnadata for motiffinder
    finderdict=Dnadata.copy()
    finderdict.pop(key)


    while i<len(value)-1:
        for start in range(0,len(value)):
            suspect=value[start:len(value)-i]

            #doesn't check for single nucleotides
            if len(suspect)>1:
                #sends substring to motiffinder function to check if its a motif
                motif=motiffinder(finderdict,suspect)

                #adds the motif to an array 
                if motif!=None:
                    hit.append(motif)
                
        i=i+1
    break

#sorts array of motifs by length
hit.sort(key=len)
         
#output longest motif
print(hit[len(hit)-1])

          
f.close()
o.close()
