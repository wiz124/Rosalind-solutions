f= open('rosalind_revc.txt','r')
o= open('output.txt', 'w')

#complementary dna
compdna=''
for line in f:
  #read string and stores to s
    s=str(line)[::-1] #[::-1] reverses a string
    print(s)

  #reads each character in the DNA strand and adds the complement to compdna
    for char in s:
        if char=='A':
             compdna+='T'
        if char=='C':
             compdna+='G'
        if char=='G':
            compdna+='C'
        if char=='T':
            compdna+='A'
    
print(compdna)
o.write(compdna)

f.close()
o.close()
