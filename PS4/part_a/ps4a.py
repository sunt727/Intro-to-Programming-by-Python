# Problem Set 4A
# Name: Tuo Sun
# Collaborators: None
# Time Spent: 0:30


# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = [[1, 10], 2]
tree2 = [[15, 9], [[9, 7], 10]]
tree3 = [[12], [2, 4, 2], [6]]


# Part A1: Multiplication on tree leaves

def mul_tree(tree):
    """
    Recursively computes the product of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the product of all leaves of the tree.

    """
    total = 1
    if tree != []:
        for i in tree:
            if type(i) == list:
                total *= mul_tree(i)
            elif type(i) == int:
                total *= i
    return total


# Part A2: Arbitrary operations on tree leaves

def addem(a,b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b

def prod(a,b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b

def operate_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """

    if tree != []:
        for i in tree:
            if type(i) == list:
                base_case = operate_tree(i, op, base_case)
            elif type(i) == int:
                base_case = op(i, base_case)
    return base_case

# Part A3: Searching a tree

def search_odd(a, b):
    """
    Operator function that searches for odd values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or odd, and False otherwise
    """
    for i in [a, b]:
        if (type(i) == int and i%2 != 0) or (type(i) == bool and i):
            return True
    return False

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # Do not erase the pass statement below.
    # print(mul_tree(tree1))
    # print(mul_tree(tree2))
    # print(mul_tree(tree3))
    # print(operate_tree(tree1, addem, 0))
    # print(operate_tree(tree2, addem, 0))
    # print(operate_tree(tree3, addem, 0))
    # print(search_odd(False, 10))
    pass