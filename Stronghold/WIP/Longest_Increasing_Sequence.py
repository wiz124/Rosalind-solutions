def increase(n, perm):
    smallest = 0
    increasing = []
    try:
        for i in range(0, int(n)):

            p = int(perm[i])
            if p > smallest and int(perm[i + 1]) > smallest and smallest < int(perm[i + 1]):
                smallest = int(perm[i + 1])
                increasing.append(smallest)
    except:
        if smallest < int(perm[len(perm) - 1]):
            increasing.append(int(perm[len(perm) - 1]))

    print(increasing)


with open('input.txt', 'r') as f:
    n = ''
    perm = []
    strings = []

    for line in f:
        strings.append(line.strip().replace(' ', ''))

    n = strings[0]
    for i in strings[1]:
        perm.append(i)

    increase(n, perm)
    perm.reverse()
    increase(n, perm)

'''
5
5 1 4 2 3
0 1 2 3 4



'''
