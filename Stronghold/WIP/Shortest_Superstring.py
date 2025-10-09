#genome assembly as shortest superstring
#derived solution
#create a table
#ie.
#  A T T A G A C C T G  (superstring)
#A 1     1   1
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

#check the diagonal to determine length of longest substring
def diagonalcheck(sub_gene,sub_superstring):


    if sub_gene[0]!=sub_superstring[0] or len(sub_gene)==1 or len(sub_superstring)==1:


        return 0
    else:
        return 1 +diagonalcheck(sub_gene[1:],sub_superstring[1:])



#checks for common character from gene to superstring, only looks for hits
def string_table(gene,x_axis_string):
    high_score=0
    substring_length=0

    for gene_index in range(0,len(gene)): #gene is y axis
        print(f'gene char {gene[gene_index]}')

        for super_index in range(0,len(x_axis_string)):  #superstring is x axis, string traversed in reverse direction

            #if matching characters appear, takes the index position and passes it through to diagonal check function
            #superstring(x_axis_string) will be traversed in the right->left direction, reverse_index will give char position
            # of such traversal

            reverse_index=len(x_axis_string)-super_index-1

            if gene[gene_index]==x_axis_string[reverse_index]:

                if super_index<len(x_axis_string) or gene_index<=len(gene):

                    print(f'substring: {gene[gene_index:]}')
                    print(f'superstring-substring: {x_axis_string[reverse_index:]}')

                    substring_length=diagonalcheck(gene[gene_index:],x_axis_string[reverse_index:])

                    print(f'length {substring_length}')
                    print(' ')

                # if substring_length > high_score:
                #     high_score = substring_length

        # print(gene_char+' '+str(high_score))



with open('input.txt','r') as f:
    geneassembly=[]
    for line in f:
        if '>' not in line:
            line=line.strip().replace(' ','')
            geneassembly.append(line)

superstring=str(geneassembly[0])
geneassembly.pop(0)

for genome in geneassembly:
    string_table(genome, superstring)


