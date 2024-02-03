f= open('input.txt','r')
o= open('output.txt', 'w')




#converts database into key/value pair
Dnadata={}
string=''
for line in f:
    #identifies if line is id line
    if '>' in line:
        Dnadata.update({line:''})
        string=line
    #identifies dna strand, also concatenates
    else:
        Dnadata.update({string:str(Dnadata[string]+line).strip()})#<---.strip
                                                                #removes whitespace

prevpercent=0
highestid=''
percentgc=1
for key,value in dict.items(Dnadata):
    #calc percent gc values
    percentgc=(float(value.count('G'))+float(value.count('C')))/float(len(value.strip()))*100

    #updates dict to percent gc value
    Dnadata.update({key:percentgc})
    
    #compares previous percent to current percent value, replaces lower value with higher value
    if prevpercent<percentgc:
        highestid=key
        prevpercent=percentgc
        
    


#prints out highest percent
print(highestid.replace('>',''))
print('%.6f'%Dnadata.get(highestid))#answer to 6 decimal places


f.close()
o.close()
