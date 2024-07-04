import re


def output(prot):
    with open('output.txt','w') as f:
        f.write(prot)

#translates then transcribes processed dna string        
def transcription(dna):
    dna=dna.replace('T','U')

    prot=''
    codontable={
        'UUU':'F',   'CUU':'L', 'AUU':'I', 'GUU':'V',
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
    
    for i in range(0,len(dna),3):
        
        if codontable[dna[i:i+3]] !='Stop':
            prot=prot+codontable[dna[i:i+3]]
            
        else:
            pass
    #print(prot)
    return prot

#concatenate processed dna string
def concat(substring):
    fullstring=''
    for i in substring:
        fullstring=fullstring+i
    #print(fullstring)
    return fullstring

#remove introns from dna sequence 
def removal(intron, dna):
    try:
        for string in dna:
            pos=dna.index(string)
            
            placeholder=re.split(intron,string)
          
            
            if len(placeholder)>1:
                dna.remove(string)
                for i in placeholder:
                    
                    dna.insert(pos,i)
                    pos+=1
        
        return dna
    
    except:
        return dna 

def main(introns,dna):
    
    splitdna=[dna]
    
    for i in introns:
       
        splitdna=removal(i,splitdna)
        
    #print(splitdna)
    output(transcription(concat(splitdna)))

        

with open('rosalind_splc.txt','r') as f:
    dna=''
    strings={}
    substrings=[]
    
    for line in f:
        if '>'  in line:
            strings.update({line:''})
            string=line
        else:
            strings.update({string:str(strings[string]+line).strip()})

    #sort out main dna sequence and substrings       
    for key, value in dict.items(strings):
        if len(strings[key])>len(dna):
            dna=strings[key]
        elif len(strings[key])<len(dna):
            substrings.append(strings[key])
            
    
    main(substrings,dna)

    
    
