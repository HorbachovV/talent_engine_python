# Parts of list

# Task:
# Write a function that gives all the ways to divide a list of at least two elements in two non-empty parts.

# Each two non empty parts will be in a tuple
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
# Example:
# >>> a = ["az", "toto", "picaro", "zone", "kiwi"]
# >>> partlist(a)

# [('az', 'toto picaro zone kiwi'), ('az toto', 'picaro zone kiwi'), ('az toto picaro', 'zone kiwi'), ('az toto picaro zone', 'kiwi')]

test_data = ["az", "toto", "picaro", "zone", "kiwi"]

def partlist(list_):
    n = len(list_)
    result = []
    for i in range(1, n):
        part1 = " ".join(list_[:i])
        part2 = " ".join(list_[i:])
        result.append((part1, part2))
    return result
	
print(partlist(test_data))
                            