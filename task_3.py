# Shwalengthimeter

# You are given with a list with strings. You need to return list with modified strings:
# • first character is removed
# • second character is removed if it is vowel("a", "e", "o", "i", "u", "y")
# • added "shwa" to the beginning
# • added " " (space) to the end
# • added length of original string to the end

# Example:
# apple -> shwapple 5
# banana ->  shwanana 6
# tractor ->  shwaractor 7
# ["garik", "balkon"] ->  ["shwarik 5", "shwalkon 6"]

test_strings = ["kawabunga", "metro2013", "moon", "orange"]

def shwalengthimeter(test_strings):
    new_list = []

    for i in test_strings:
        length = len(i)
        i = i[1:]
        if i[0] in ["a", "e", "o", "i", "u", "y"]:
            i = i[1:]
        new_list.append('shwa' + i + " " + str(length))

    return new_list


print(shwalengthimeter(test_strings))