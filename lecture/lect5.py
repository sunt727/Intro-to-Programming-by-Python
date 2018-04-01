# -*- coding: utf-8 -*-

  
#seq = (2, 'a', 4, (1, 2))
#print(len(seq))
#print(seq[2] + 1)
#print(seq[3])
#i = 2
#print(seq[i - 1])
#print(seq[-1])
##print(seq[4])
#
#print(seq[1])
#print(seq[:-1])
#print(seq[1:3])
#
#for e in seq:
#    print(e)

#L = [1,2,3,4]
#for i in range(len(L)):
#    L.append(i)
#print(i)

#L1 = [0,3,-2]
#L2 = ['President', 'Abraham', 'Lincoln']
#s = ''
#for i in range(len(L1)):
#    s += L2[i][L1[i]]
#print(s)

# L = [1,2,3,4]
# i = 0
# for e in L:
#    L.append(i)
#    i += 1
# print(i)

# L = [1,2,3,4]
# i = 0
# for e in L:
#    L = L + L
#    i += 1
# print(L)

#L = [2,1,3,6,3,7,0] 
#L.pop(5)
#print(L)
#L.remove(3)
#print(L)
#L.pop()
#print(L)

#def remove_dups(L1, L2):
#    for e in L1:
#        if e in L2:
#            L1.remove(e)
#
#L1 = [1, 2, 3, 4]
#L2 = [1, 2, 5, 6]
#remove_dups(L1, L2)
#print(L1)

#def mult_iter(a, b):
#    result = 0
#    while b > 0:
#        result += a
#        b -= 1
#    return result

#def fact(n):
#    if n == 1:
#        return 1
#    else:
#        return n*fact(n-1)
#
#print(fact(4))

#def find_elem_recur(e, L):
#    if L == []:
#        return False
#    elif len(L) == 1:
#        return L[0] == e
#    else:
#        half = len(L)//2
#        if L[half] > e:
#            return find_elem_recur(e, L[:half])
#        else:
#            return find_elem_recur(e, L[half:])
#
#L = [1,2,3,5,6,7,8]
#print(L)
#print(find_elem_recur(4, L))