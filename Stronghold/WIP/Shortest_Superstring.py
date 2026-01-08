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

#module more efficiently reads fasta files
from Bio import SeqIO

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
    longest_length=0

    for i in range(len(sub_gene)):
        if sub_gene[:i] in sub_superstring and longest_length<len(sub_gene[:i]):
            longest_length=len(sub_gene[:i])
        else:
            continue
    return longest_length

#recursive solution for funsies
    # if sub_gene[0]!=sub_superstring[0]:
    #
    #     return 0
    # elif len(sub_gene)==1 or len(sub_superstring)==1:
    #     return 1
    # else:
    #     return 1 +diagonalcheck(sub_gene[1:],sub_superstring[1:])
def if_overlap(gene, superstring):
    gene_firsthalf=gene[:len(gene)//2]
    gene_secondhalf=gene[len(gene)//2:]
    if gene_firsthalf not in superstring and gene_secondhalf not in superstring:
        return 3
    elif gene_firsthalf in superstring:
        return 1
    elif gene_secondhalf in superstring:
        return 2

#checks for common character from gene to superstring, only looks for hits
def string_table(gene, superstring):
    temp_length=0
    substring_pos=[]


    for gene_index in range(0,len(gene)): #gene is y axis

            for super_index in range(0, len(superstring)):  #superstring is x axis, string traversed in reverse direction
                reverse_index = len(superstring) - super_index - 1
                #if matching characters appear, takes the index position and passes it through to diagonal check function
                #superstring(x_axis_string) will be traversed in the right->left direction, reverse_index will give char position
                # of such traversal


                if gene[gene_index]==superstring[reverse_index]:

                    if super_index<len(superstring) or gene_index<=len(gene):

                        substring_length=diagonalcheck(gene[gene_index:], superstring[reverse_index:])

                        if temp_length<substring_length:
                            temp_length=substring_length
                            end_index=gene_index+substring_length
                            start_index=gene_index
                            substring_pos=[start_index,end_index,True]


                else:
                    continue


    return substring_pos

def Main():
    with open('input.txt','r') as f:
        geneassembly=[]
        for entry in SeqIO.parse(f,'fasta'):
            geneassembly.append(str(entry.seq))

    superstring=geneassembly[0]
    geneassembly.pop(0)


    while len(geneassembly)!=0:
        genome=geneassembly[0]
            #string_table will check for the substring pos if there is one
        if genome in superstring:
            geneassembly.remove(genome)
            continue
        else:
            # substring_coord=string_table(genome, superstring)
            check=if_overlap(genome,superstring)
            if check !=3:
                substring_coord=string_table(genome,superstring)
                superstring=string_concat(substring_coord,genome,superstring)
                geneassembly.remove(genome)
            else:
                geneassembly.remove(genome)
                geneassembly.append(genome)
            # if not substring_coord:
            #
            #     geneassembly.remove(genome)
            #     geneassembly.append(genome)


            # elif substring_coord[2]:
            #     superstring=string_concat(substring_coord,genome,superstring)
            #     geneassembly.remove(genome)


    output(superstring)

Main()
