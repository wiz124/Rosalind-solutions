f= open('rosalind_prot.txt','r')
o= open('output.txt', 'w')

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



rna=''
for line in f:
    rna=rna+line

codon=''
proteinstring=''
i=0

while i<len(rna)-1:
    codon=rna[i]+rna[i+1]+rna[i+2]
    for key,value in dict.items(codontable):
        if key==codon:
            if value!='Stop':
                proteinstring=proteinstring+value
                break
    i=i+3


print(proteinstring)

f.close()
o.close()
