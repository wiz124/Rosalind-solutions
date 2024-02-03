#goal is to extract fasta data from uniprot db and find the motif locations in
#the protein sequence

#allows use of end='' 
from __future__ import print_function

#needed to access db
import urllib
import contextlib

#regex python searches for set pattern of characters
#regex stands for regular expression
#searching through iteration of sequence doesn't work for some reason
import re 

#method to extract data from uniprot fasta
def readuniprotfasta(proteinurl):
    sequence=''

    #use the with statement for future access to uniprot database for fasta files
    with contextlib.closing(urllib.urlopen(proteinurl)) as f:
         #extracting the protein seq from fasta   
         for line in f:
             if '>' not in line:
                 sequence=sequence+line.strip()

    return sequence


#motif sequence=N{P}[ST]{P}
#motif reqex search sequence=N[^P][ST][^P]           
def motiffinder(sequence,line, protein):

    finallist=[]
    for i in range(0, len(sequence)):

        #regex can't do repeat searches on strings that have been a match
        #requires iteration through string to search for all possible hits
        hitlist=re.findall('N[^P][ST][^P]',sequence[i:len(sequence)])

        #combine each list from iterating
        finallist=finallist+hitlist
        
        #converts to dict then list type to remove duplicates
        finallist=list(dict.fromkeys(finallist))

    location=[]
    for i in finallist:
        location.append(sequence.find(i)+1)
    location.sort()          


    output(location,protein)

    
   
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
with open('input.txt','r') as f:
    for line in f:
        protein=line
        if '_' in line:

            #removes characters from underscore and beyond
            protein=line.split('_',1)[0]
            
        #need correct url to access fasta file    
        proteinurl='http://www.uniprot.org/uniprot/'+protein.strip()+'.fasta'
        
        #method to extract fasta file contents and search for motif
        motiffinder(readuniprotfasta(proteinurl),protein,line)

