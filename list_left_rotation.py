# List left rotation

# This is very common task - to shift part of list from the beginning to end. You need to write a function which will take a list and some int (which will be less than a length of list) and return new left-rotated list.

# For example you have a list list_ which is of length 5. You run your function on it and set number of rotations to 3:

# list_  = [1, 2, 3, 4, 5]
# rotation = 3
# print(left_rotate(list_, rotation)) 
# # should produce:
# [4, 5, 1, 2, 3]

list_ = list("1234567")

def left_rotate(l, num):
    # ...solution...
    if num >= len(l):
        return l
    return l[num:] + l[:num]

# Tests:
print(left_rotate(list_, 4)) # should be ["5", "6", "7", "1", "2", "3", "4"]
print(left_rotate(list_, 5) is not list_) # should be True