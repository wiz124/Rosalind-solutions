#global array for output
finallist=[]

#translates codon sequence
def protein(codon):
    #codon table
    codontable={
        'UUU':'F',   'CUU':'L', 'AUU':'I', 'GUU': 'V',
        'UUC':'F',   'CUC':'L', 'AUC':'I', 'GUC':'V',
        'UUA':'L',   'CUA':'L', 'AUA':'I', 'GUA':'V',
        'UUG':'L',   'CUG':'L', 'AUG':'M', 'GUG':'V',
        'UCU':'S',   'CCU':'P', 'ACU':'T', 'GCU':'A',
        'UCC':'S',   'CCC':'P', 'ACC':'T', 'GCC':'A',
        'UCA':'S',   'CCA':'P', 'ACA':'T', 'GCA':'A',
        'UCG':'S',   'CCG':'P', 'ACG':'T', 'GCG':'A',
        'UAU':'Y',   'CAU':'H', 'AAU':'N', 'GAU':'D',
        'UAC':'Y',   'CAC':'H', 'AAC':'N', 'GAC':'D',
        'UAA':'Stop','CAA':'Q', 'AAA':'K', 'GAA':'E',
        'UAG':'Stop','CAG':'Q', 'AAG':'K', 'GAG':'E',
        'UGU':'C',   'CGU':'R', 'AGU':'S', 'GGU':'G',
        'UGC':'C',   'CGC':'R', 'AGC':'S', 'GGC':'G',
        'UGA':'Stop','CGA':'R', 'AGA':'R', 'GGA':'G',
        'UGG':'W',   'CGG':'R', 'AGG':'R', 'GGG':'G'}
    return codontable[codon]
    
   

#convert DNA to RNA to protein
def conversion(dna):
    
    dna=dna.replace('T','U')
    
    proteinlist=[]
    seq=''
    
    for i in range(len(dna)):
        try:
          
          #search for start codon
            if dna[i]+dna[i+1]+dna[i+2]=='AUG':
                
                for j in range(i,len(dna),3):
                    
                    aa=protein(dna[j:j+3])
                   
                    if aa!='Stop':
                        seq=seq+aa
                    
                    elif aa=='Stop':
                        #adds stop to sequence for later filtering
                        seq=seq+aa
                        break
                
                    
            else:
                continue
        except:
           break 
            
        if seq!='':
            proteinlist.append(seq)
            seq=''
        else:
            pass
      
        
    return proteinlist
    
    

#sorts out results
def output(protein_seq):
    
    for i in protein_seq:
      #filter out sequences without stop codons
        if i[-4:]=='Stop':
            i=i[:len(i)-4]
            if i not in finallist:
                finallist.append(i)
        
    print(finallist)
    with open ('output.txt', 'w') as f:
        for j in finallist:
            f.write(j+'\n')
    
#retrieve dna string
with open('rosalind_orf.txt','r') as f:
    dna=''
    for line in f:
        if '>' in line:
            pass
        else:
            dna=dna+line.strip()

    dna=dna.strip()
 

    #converts sequence
    output(conversion(dna))

    #converts reverse complement
    output(conversion(dna[::-1].replace('T','a').replace('A','t').replace('G','c').replace('C','g').upper()))
    
