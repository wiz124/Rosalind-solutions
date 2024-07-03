def output(position, length):
    with open('output.txt', 'w') as f:
        
        for i in range(0,len(position)):
            f.write(str(position[i])+' '+str(length[i])+'\n')
        
    
#iterate all possible substrings with length 4 to 12 bp
def substring(seq):
    position=[]
    length=[]
    hits=[]

    
    for start in range(0,len(seq)):
        for i in range(4,13):  
            sub=seq[start:start+i]
            
            complement=reverse(sub)[::-1]
        
            if len(sub)<4:
                continue
            else:
                if complement==sub and start+i<=len(seq):
                    
                    hits.append(sub)
                    position.append(start+1)
                    length.append(i)
                    
                else:
                    pass
                
    output(position, length)
   
            
#gives reverse complement    
def reverse(seq):
    seq=seq.replace('T','a').replace('A','t').replace('G','c').replace('C','g').upper()
    return seq
    

with open('rosalind_revp.txt', 'r') as f:
    seq=''
    for line in f:
        if '>' in line:
            pass
        else: seq=seq+line.strip()
        
substring(seq)



