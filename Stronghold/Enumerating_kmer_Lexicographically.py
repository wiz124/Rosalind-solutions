import itertools

def output(strings):
    with open('output.txt', 'w') as f:
        for string in strings:
            f.write(string+'\n')
            

def combination(length,symbols):
    
    #this thing autosorts it alphabetically 
    combo=itertools.product(symbols, repeat=length)

    strings=[]
    for i in combo:
        strings.append(''.join(i))

    #print(strings)
    return strings        


with open('rosalind_lexf.txt','r') as f:
    symbols=[]
    integer=0
    
    for line in f:
        
        #remove blank spaces
        line=line.replace(' ','').strip()

        #check for digits in the string        
        if any(char.isdigit() for char in line):
               integer=line
        else:
            for char in line:
                symbols.append(char)


    output(combination(int(integer),symbols))    
    
