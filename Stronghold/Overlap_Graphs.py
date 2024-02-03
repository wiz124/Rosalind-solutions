f= open('rosalind_grph (1).txt','r')
o= open('output.txt', 'w')

#converts database into key/value pair
Dnadata={}
string=''
for line in f:
    #identifies if line is id line
    if '>' in line:
        line=line.replace('>','')
        Dnadata.update({line:''})
        string=line
    #identifies dna strand, also concatenates
    else:
        Dnadata.update({string:str(Dnadata[string]+line).strip()})#<---.strip
                                                                #removes whitespace
v=[]
w=[]
#remove any s=t
for key, value in dict.items(Dnadata):
    if value[:3]==value[-3:]:
        Dnadata.pop(key)
    for i,k in dict.items(Dnadata):
        if i!=key:
            if value[:3]==k[-3:]:
                v.append(i)
                w.append(key)
            
for number in range(0,len(v)):
    o.write(v[number].strip()+' '+w[number])
    #print(v[number].strip()+' '+w[number])

f.close()
o.close()
