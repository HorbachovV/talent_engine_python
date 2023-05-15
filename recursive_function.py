# Recursive function

# Recursive function calls itself. The classic example is factorial calculation:

# def fact(x):                
#     "1 * ( 2 * ( 3 * 4))"   
#     if x == 1:              
#         return 1            
#     else:                   
#         return x * fact(x-1)
# Using recursive function gives this bonuses: * Recursive functions make the code look clean and elegant. * A complex task can be broken down into simpler sub-problems using recursion. * Sequence generation is easier with recursion than using some nested iteration.

# The task here is to write recursive function which will calculate sum of all numbers in this list:

# [1, [2, [3], 4]] # 10 
# [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]] # 72
# Additional task: write the same using just string processing (i.e. without recursively called functions but using only manipulations on the string) and compare - what approach is faster?

list_ = [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

def rec_func(list_):
    #....
    total = 0
    for item in list_:
        if type(item) == list:
            total += rec_func(item)
        else:
            total += item
    return total

print (rec_func(list_))