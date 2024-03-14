#goal is to extract fasta data from uniprot db and find the motif locations in
#the protein sequence

#allows use of end='' 
from __future__ import print_function

#needed to access db
import urllib.request
import contextlib


#regex python searches for set pattern of characters
#regex stands for regular expression
#searching through iteration of sequence doesn't work for some reason
import re 

#method to extract data from uniprot fasta
def readuniprotfasta(proteinurl):
    sequence=''

   #opens and reads protein sequence from fasta file
    for line in urllib.request.urlopen(proteinurl):
        #removes other garbage from fasta file
        if '>' in str(line):
            pass
        else:
            sequence=sequence+line.decode('utf-8').strip()


    #print(sequence)
    
    return sequence


#motif sequence=N{P}[ST]{P}
#motif reqex search sequence=N[^P][ST][^P]           
def motiffinder(sequence,line, protein):

    finallist=[]
    i=0
    while i <=len(sequence):
        #regex can't do repeat searches on strings that have been a match
        #requires iteration through string to search for all possible hits
        hitlist=re.search('N[^P][ST][^P]',sequence[i:len(sequence)])

    
     #try except block incase re.search comes up with nothing
        try:
            #add i so no same sequence found over and over
            finallist.append(int(hitlist.start())+i+1)
       
            #converts to dict then list type to remove duplicates
            finallist=list(dict.fromkeys(finallist))
            i=i+int(hitlist.start())+1
        except:
            i+=1
            pass

    
    #print(finallist)

    output(finallist,protein)

    
   
#output to file         
def output(location, protein):
    
    #if no motifs, just skips
    if not location:
        pass
    
    else:
        #print(protein)
        #print(location)
        with open('output.txt', 'a') as o:
            o.write(('\n'+protein).strip())
            o.write('\n'+' '.join([str(pos) for pos in location])+'\n')
            

#'with' keyword opens up file and closes it automatically 
with open('rosalind_mprt.txt','r') as f:
    for line in f:
        protein=line
        if '_' in line:

            #removes characters from underscore and beyond
            protein=line.split('_',1)[0]
            
        #need correct url to access fasta file    
        proteinurl='http://rest.uniprot.org/uniprotkb/'+protein.strip()+'.fasta'
        
        #method to extract fasta file contents and search for motif
        motiffinder(readuniprotfasta(proteinurl),protein,line)
