f= open('input.txt','r')
o= open('output.txt', 'w')

#factorial calcs
def factorial(n):

    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))
#solves for nCx function
def combination(n,x):
    product=factorial(n)/(factorial(n-x)*factorial(x))
    return product

#data input
param=[]
for line in f:
    for word in line.split():
            param.append(word)
        
k=int(param[0])
n=int(param[1])

AaBb=float(.25)

total=2**k

probability=0

#binomial probability calculation
for i in range(n,total+1):
    probability=probability+combination(total,i)*(AaBb**i)*((1-AaBb)**(total-i))



print(round(probability,3))
f.close()
o.close()
