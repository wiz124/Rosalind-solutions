#genome assembly as shortest superstring
#derived solution
#create a table
#ie.
#  A T T A G A C C T G
#A 1     1
#G         1         1
#A 1     1   1
#C             1 1
#C             1 1
#T   1 1           1
#G         1         1
#C             1 1
#C             1 1
#G         1          1
#
# from the table, we see longest diagonal is the longest common substring
#compare indices from each string, largest index value gets appended to by the string with smallest index value
        # if same index value, then same string


def largestsimilarity(gene,superstring):
    for i in range(0,len(gene)):
        substring=gene[:i]


with open('input.txt','r') as f:
    geneassembly=[]
    for line in f:
        if '>' not in line:
            line=line.strip().replace(' ','')
            geneassembly.append(line)

superstring=str(geneassembly[0])
geneassembly.pop(0)

for genome in geneassembly:
    largestsimilarity(genome, superstring)


