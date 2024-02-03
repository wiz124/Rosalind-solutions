f= open('rosalind_hamm (1).txt','r')
o= open('output.txt', 'w')


strand1=''
strand2=''
strand3=''

#retrieve input, combines input into one string
for line in f:
    strand1=strand1+line
    strand1=strand1.strip()

print(len(strand1))
print(strand1)
#splitting input into two parts
strand2=strand1[0:len(strand1)/2].strip()
strand3=strand1[len(strand1)/2:len(strand1)].strip()

print(strand2)
print(strand3)

hammdist=0
i=0
#traverse across strand length and compare
while i<len(strand2):
    if strand2[i]!=strand3[i]:
        hammdist+=1
    i+=1

    
o.write(str(hammdist))
print(hammdist)

f.close()
o.close()
