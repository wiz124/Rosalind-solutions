def totalstrings(aminoacid):

    #codon table copied from previous work 
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

    codons=[]
    possiblestrings=3 #start with 3 because 3 possible stop codons
    
    #find how many codons correspond to which aa
    for char in aminoacid:
        codons.clear()
        for key,value in dict.items(codontable):
            if value == char:
                codons.append(key)
        #multiply to find possible combinations
        possiblestrings=possiblestrings*len(codons)

    print(possiblestrings)

#input
with open('input.txt','r') as f:
    aminoacids=''
    for line in f:
        aminoacids=aminoacids+line.strip()

    totalstrings(aminoacids)

