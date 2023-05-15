# Remove Smallest +

# Remove several (given number) - smallest - items from given list.

# Don't modify original list and preserve original order. First parameter is number of items to remove, second one - original list.

# remove_smallest(3, [1,2,3,1,2,4]) --> [3, 2, 4]

tests = [
    (3, [1,2,3,1,2,4], [3,2,4]), 
    (2, [5,4,1,3], [5,4]), 
    (4, [1,2,1], [])
]

def remove_smallest(num, list_):
    new_list = list(list_)
    sorted_list = sorted(new_list)
    indices_to_remove = sorted_list[:num]
    for index in indices_to_remove:
        new_list.remove(index)
    return new_list

for test in tests:
    number, original, expected = test
    actual = remove_smallest(number, original)
    assert actual == expected, "Wrong :("
    assert actual is not original, "You can't change original list"