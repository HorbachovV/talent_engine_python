# Greetings

# Hello, in this task you should greet people found from kind-of-CSV file.

# You're given with a comma-separated string with names of people you should greet. Each name is in form: Mr__John_Smith, so __ should be replaced by a dot and space, and _ should be replaced with a space. The program (function greet_people() should take given input list and output a list with strings like this one: "Hello, Mr. John Smith!".

# As an example input data:

# names = "Mr__John_Smith, Ms__Samantha_Wolf"
# Running greet_people(names) should return:

#  ['Hello Mr. John Smith!', 'Hello Ms. Samantha Wolf!']

names = "Mr__John_Smith, Ms__Samantha_Wolf,Mrs__Violetta_Ford,Mr__Duglas_Adams"

# Place solution in the following function (and remove this line):
def greet_people(names):
    return []
    
print("\n".join(greet_people(names)))