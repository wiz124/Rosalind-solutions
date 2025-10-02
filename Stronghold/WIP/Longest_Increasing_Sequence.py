#algorithm

#def Main(n, perm):
#    for i in perm:






#parse input file
with open('input.txt', 'r') as f:

    n = 0
    perm = []
    strings = []

    for line in f:
        strings.append(line.strip())


#convert everything to int
    n = int(strings[0])
    perm=list(map(int,strings[1].split(' ')))

    #Main(n,perm)
    

'''
5
5 1 4 2 3
0 1 2 3 4



'''
