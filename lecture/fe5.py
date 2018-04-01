listA, listB = [1, 2, 3], [4, 5, 6]

sum = 0

for i in listA:
    j  = listB[listA.index(i)]
    sum += i*j

print (sum)


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here

    sum = 0

    for i in listA:
        j = listB[listA.index(i)]
        sum += i * j

    return sum

numsList = [3,4,0,2,1,9,25]

def countSqrts(numsList):
    '''
    numsList: a list
    '''
    # Your code here
    count = 0

    for i in numsList:
        if numsList.count(i**2) > 0:
            count += 1

    return count


print(countSqrts(numsList))

