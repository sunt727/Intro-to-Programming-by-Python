# # # def keysWithValue(aDict, target):
# # #     '''
# # #     aDict: a dictionary
# # #     target: an integer or string
# # #     '''
# # #     # Your code here
# # #
# # #     key_list = []
# # #     for i in list(aDict.keys()):
# # #         if aDict[i] == target:
# # #             key_list.append(i)
# # #
# # #     return sorted(key_list)
# # #
# # #
# # # def recurPower(base, exp):
# # #     '''
# # #     base: int or float.
# # #     exp: int >= 0
# # #
# # #     returns: int or float, base^exp
# # #     '''
# # #     # Your code here
# # #
# # #     if exp > 0:
# # #         return base * recurPower(base, exp-1)
# # #     else:
# # #         return 1
# # #
# # # print(recurPower(10,10))
# # #
# # L1 = [1,2,3]
# # L2 = [1,3,1]
# #
# # def diffs(L1, L2):
# #     '''
# #     Assumes: L1 and L2 are non-empty lists of the same length of ints
# #     Effects: returns the sum of the pairwise differences of L1 - L2.
# #     For example, if L1 = [1,2,3] and L2 = [1,3,1] it returns 1. (Because
# #     (1-1) + (2-3) + (3-1) = 1.)
# #     '''
# #     # Your code here
# #     sum = 0
# #     for i in range(len(L1)):
# #         sum += (L1[i] - L2[i])
# #
# #     return sum
# #
# # print(diffs(L1, L2))
# #
# # L = [1, [], [1,2]]
# #
# # def getShortest(L):
# #     '''
# #     Assumes: L is a list, each element of which is either a list or an int
# #     Effects: Returns None if L does not contain a list, otherwise returns
# #     the length of the shortest list in L. E.g., if L = [1, [], [1,2]] it
# #     returns 0.
# #     '''
# #     # Your code here
# #
# #     len_list =[]
# #
# #     for i in L:
# #         if type(i) == list:
# #             len_list.append(len(i))
# #
# #     return None if len_list == [] else min(len_list)
# #
# # print(getShortest(L))
#
# # class Weird(object):
# #     def __init__(self, x, y):
# #         self.y = y
# #         self.x = x
# #     def getX(self):
# #         return x
# #     def getY(self):
# #         return y
#
# class Wild(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#
# X = 7
# Y = 8
#
# # w1 = Weird(X, Y)
# # print(w1.getX())
# # print(w1.getY())
#
# w2 = Wild(X, Y)
# print(w2.getX())
#
# print(w2.getY())
# w3 = Wild(17, 18)
# print(w3.getX())
# print(w3.getY())
# w4 = Wild(X, 18)
# print(w4.getX())
# print(w4.getY())
# X = w4.getX() + w3.getX() + w2.getX()
# print(X)
# print(w4.getX())
# Y = w4.getY() + w3.getY()
# Y = Y + w2.getY()
# print(Y)
#
# class Container(object):
#     '''
#     A container object is a list and can store elements of any type
#     '''
#     def __init__(self):
#         '''
#         Initializes an empty list
#         '''
#         self.myList = []
#
#     def size(self):
#         '''
#         Returns the length of the container list
#         '''
#
#         return len(self.myList)
#
#     def add(self, elem):
#         '''
#         Adds the elem to one end of the container list, keeping the end
#         you add to consistent. Does not return anything
#         '''
#         self.myList.append(elem)
#
# class Stack(Container):
#     '''
#     A subclass of Container. Has an additional method to remove elements.
#     '''
#     def remove(self):
#         '''
#         The newest element in the container list is removed
#         Returns the element removed or None if the queue contains no elements
#         '''
#         return self.myList.pop(-1) if self.size() > 0 else None
#
# class Queue(Container):
#     '''
#     A subclass of Container. Has an additional method to remove elements.
#     '''
#     def remove(self):
#         '''
#         The oldest element in the container list is removed
#         Returns the element removed or None if the stack contains no elements
#         '''
#         return self.myList.pop(0) if self.size() > 0 else None
def f(s):
    dict = {}
    for i in set(s):
        dict[i] = list(s).count(i)
    return dict

def sumList(L):
    '''
    Assumes: L is a list.
    Effects: returns a float that is the sum of all of the
             numbers and strs in L that can be converted to
             floats.
             if L contains no numbers, raises ValueError
             For example, sumList([1, 2, 'a', '1.5', 3.5])
             returns 8.0
    '''

    sum_all = 0
    is_digits_in = False
    for i in L:
        try:
            sum_all += float(i)
            if type(float(i)) == float:
                is_digits_in = True
        except:
            pass
    if is_digits_in == False:
        raise ValueError
    return sum_all




L = [1, 2, 'a', '1.5', 3.5]
M = ['a','b']
print(sumList(L))
print(sumList(M))