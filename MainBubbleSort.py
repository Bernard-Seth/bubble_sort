import random

groupSize = int(input('How many numbers are we sorting today?'))

numSet = random.sample(range(0, 999999), groupSize)
print('Our set of numbers is' + str(numSet))

def sort(arr, i, j, k):
    for i in range(j):
        for k in range(0, j-i-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]


sort(numSet, 0, groupSize, 0)

print('Our sorted numbers are')
for i in range(groupSize):
    print(numSet[i])