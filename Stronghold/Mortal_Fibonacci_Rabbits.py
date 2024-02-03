f= open('rosalind_fibd (1).txt','r')
o= open('output.txt', 'w')

#algo
def MortalFibonacci(n, m):
    living = [1, 1]
    for i in range(2, n):
        print('i: '+str(i))

        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        print(living[i-1])
        print(living[i-2])
        print('tmp: '+str(tmp))
      
        # then death
        if i == m:
            tmp = tmp - 1
        print('tmp: '+str(tmp))    
        if i > m:
            tmp = tmp - living[i - m - 1]
            print(tmp)
        living.append(tmp)
    return living[-1]


#n=number of months
#m=lifespan of rabbit(months)
param=[]

#reading inputs
for line in f:
    for word in line.split():
            param.append(word)
        
n=int(param[0])
m=int(param[1])


print(MortalFibonacci(n,m))
#o.write(str(population-deaths))

f.close()
o.close()
