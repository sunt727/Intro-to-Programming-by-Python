def newSort(L):
    sum = 0
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                sum += 1
                temp = L[i]
                L[i] = L[j]
                L[j] = temp

            j += 1
    return sum

def selSort(L):
    sum = 0
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            sum += 1
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            sum += 1
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

    return sum

L=[100,22, 19, 15, 13, 11, 0]
M=[100,22, 19, 15, 13, 11, 0]
print(selSort(L))
print(newSort(M))
print(L)
print(M)