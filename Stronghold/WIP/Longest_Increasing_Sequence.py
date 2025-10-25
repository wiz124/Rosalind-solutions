# algorithm
# 9
# 8 2 1 6 5 7 4 3 9
#
#iterate through each integer in the list(doing nested for loop)
#               one to iterate for each int in the list
#               have another loop iterate through the list for every index after array[i]
# initialize lis=[] and new_lis=[]
#find longest possible subseq for array[i]
#
#
#

def longest_seq(n,arr):

    LIS=[]

    #iterate through every number in array
    for i in range(0,n):

        possible_seq=[arr[i]]*(len(arr)-1-arr.index(i))

        temp_arr=[arr[i]]

        #iterate through every number after index position of number
        for j in range(arr[i]+1,n):

            #check if next element greater than element  at index i
            if arr[j]>arr[i]:

                if arr[j]>temp_arr[-1]:
                    temp_arr.append(arr[j])
                else:
                    pass








#parse input file
with open('input2.txt', 'r') as f:

    perm = []
    strings = []

    for line in f:
        strings.append(line.strip())

#convert everything to int
n = int(strings[0])

    #map(function, iterable,...) applies function to each iterable
perm=tuple(map(int,strings[1].split(' ')))

longest_seq(n,perm)




