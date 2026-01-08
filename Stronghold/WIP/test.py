from Bio import SeqIO
with open('input.txt', 'r') as f:
    database=[]
    for entry in SeqIO.parse(f, 'fasta'):
        database.append(entry.seq)
# print(database)
gene=database[1]
superstring=database[0]
print(superstring)
print(gene)
print(gene[:len(gene)//2])
print(gene[len(gene)//2:])

