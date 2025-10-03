#genome assembly as shortest superstring
#derived solution
#create a table
#ie.
#  A T T A G A C C T G  (superstring)
#A 1     1
#G         1         1
#A 1     1   1
#C             1 1
#C             1 1
#T   1 1           1
#G         1         1
#C             1 1
#C             1 1
#G         1         1
#(gene)
# from the table, we see longest diagonal is the longest common substring
#compare indices from each string, largest index value gets appended to by the string with smallest index value
        # if same index value, then same string

#global variables
superstring=''

#check the diagonal to determine length of longest substring
def diagonalcheck(sub_gene,sub_superstring):


    if sub_gene[0]!=sub_superstring[0] or len(sub_gene)==1 or len(sub_superstring)==1:


        return 0
    else:
        return 1 +diagonalcheck(sub_gene[1:],sub_superstring[1:])



#checks for common character from gene to superstring, only looks for hits
def string_table(gene,superstring):
    high_score=0
    substring_length=0

    for gene_char in gene: #gene is y axis

        for super_char in superstring:  #superstring is x axis, traversed per char in gene

            if gene_char==super_char:

                gene_char_index= gene.index(gene_char)+1
                super_char_index= superstring.index(super_char)+1

                if super_char_index<=len(superstring) or gene_char_index<=len(gene):
                    substring_length=diagonalcheck(gene[gene_char_index:],superstring[super_char_index:])

                if substring_length > high_score:
                    high_score = substring_length

        print(gene_char+' '+str(high_score))



with open('input.txt','r') as f:
    geneassembly=[]
    for line in f:
        if '>' not in line:
            line=line.strip().replace(' ','')
            geneassembly.append(line)

superstring=str(geneassembly[0])
geneassembly.pop(0)

#print(superstring)

for genome in geneassembly:
    #print(genome)
    string_table(genome, superstring)


