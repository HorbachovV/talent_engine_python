# Only Evens

# The task is to filter out only evens (by value and their index both at the same time) from the list of integers.

# Here is the example of what does this mean - let's take a list [2, 3, 4, 5, 6] and analyse each item:

# index: 0(even) --> 2(even)
# index: 1(odd) --> 3(odd)
# index: 2(even) --> 4(even)
# index: 3(odd) --> 5(odd)
# index: 4(even) --> 6(even)
# As we can see only 2, 4 and 6 are even by value and index at the same time.

# More examples showing how function should behave:

# get_only_evens([1, 3, 2, 6, 4, 8])  # [2, 4]
# get_only_evens([0, 1, 2, 3, 4])     # [0, 2, 4]
# get_only_evens([1, 2, 3, 4, 5])     # []
# get_only_evens([])                  # []

def get_only_evens(list_: list) -> list:
    return [num for index, num in enumerate(list_) if num % 2 == 0 and index % 2 == 0]
    
    
assert get_only_evens([1, 3, 2, 6, 4, 8]) == [2, 4], "Wrong, #1"
assert get_only_evens([0, 1, 2, 3, 4]) == [0, 2, 4], "Wrong, #2"
assert get_only_evens([1, 2, 3, 4, 5]) == [], "Wrong, #3"
assert get_only_evens([]) == [], "Wrong, #4"                                   