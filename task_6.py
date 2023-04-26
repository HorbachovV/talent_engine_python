# Remove smallest

# Remove only one smallest - item from given list.

# NOTES:

# Important -- Don't modify original list and preserve original order. 
# If the smallest item is repeated only the first it's appearance should be removed
# Examples:

# remove_smallest([1,2,3,1,2])   # [2, 3, 1, 2]
# remove_smallest([5, 10, 3, 5, 3])   # [5, 10, 3, 5]

tests = [([1,2,3,4,5], [2,3,4,5]), ([5,4,1,3], [5,4,3]), ([1,2,1], [2,1])]

def remove_smallest(list_):
    copy_list = list(list_)
    if not copy_list:
        return copy_list

    min_index = copy_list.index(min(copy_list))

    copy_list.pop(min_index)
    return copy_list

for test in tests:
    result = remove_smallest(test[0])
    assert result == test[1], "Wrong :("
    assert result is not test[0], "You can't change original list"