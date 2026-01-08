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
#
#superstring creation
#     3     9
# att agacctg      superstring
#     agacctg ccg  gene
#     0     6
#
#
#     0
#     agacctg ccg superstring
# att agacctg     gene
#     3
# from the table, we see longest diagonal is the longest common substring
#compare indices from each string, largest index value gets appended to by the string with smallest index value
        # if same index value, then same string
#------------------------#
#global variables
superstring=''
#------------------------#
def output(superstring):
    with open('output.txt','w') as f:
        f.write(superstring)


#concatenates the substring to the superstring
def string_concat(substring, genome,superstring):

    #substring pos in relation to gene, NOT SUPERSTRING
    #takes a look at pos of the first char in substring in gene,
    #if start at 0, appends end of gene
    #if start not at 0, appends superstring to gene
    if substring[0]==0:
        superstring=superstring+genome[substring[1]:]
    else:
        superstring=genome[:substring[0]]+superstring

    return superstring



#check the diagonal to determine length of longest substring
def diagonalcheck(sub_gene,sub_superstring):


    if sub_gene[0]!=sub_superstring[0]:

        return 0
    elif len(sub_gene)==1 or len(sub_superstring)==1:
        return 1
    else:
        return 1 +diagonalcheck(sub_gene[1:],sub_superstring[1:])



#checks for common character from gene to superstring, only looks for hits
def string_table(gene,x_axis_string):
    temp_length=0
    substring_pos=[]


    for gene_index in range(0,len(gene)): #gene is y axis

            for super_index in range(0,len(x_axis_string)):  #superstring is x axis, string traversed in reverse direction

                #if matching characters appear, takes the index position and passes it through to diagonal check function
                #superstring(x_axis_string) will be traversed in the right->left direction, reverse_index will give char position
                # of such traversal

                reverse_index=len(x_axis_string)-super_index-1

                if gene[gene_index]==x_axis_string[reverse_index]:

                    if super_index<len(x_axis_string) or gene_index<=len(gene):

                        substring_length=diagonalcheck(gene[gene_index:],x_axis_string[reverse_index:])

                        if temp_length<substring_length and substring_length>len(gene)//2:
                            temp_length=substring_length
                            end_index=gene_index+substring_length
                            start_index=gene_index
                            substring_pos=[start_index,end_index,True]

                else:
                    continue


    return substring_pos

#global frame
with open('rosalind_long.txt','r') as f:
    geneassembly=[]
    for line in f:
        if '>' not in line:
            line=line.strip().replace(' ','')
            geneassembly.append(line)

superstring=str(geneassembly[0])
geneassembly.pop(0)


while len(geneassembly)!=0:
    genome=geneassembly[0]
        #string_table will check for the substring pos if there is one
    if genome in superstring:
        geneassembly.remove(genome)
        continue

    substring_coord=string_table(genome, superstring)

    if not substring_coord:

        geneassembly.remove(genome)
        geneassembly.append(genome)


    elif substring_coord[2]:
        superstring=string_concat(substring_coord,genome,superstring)
        geneassembly.remove(genome)


output(superstring)



