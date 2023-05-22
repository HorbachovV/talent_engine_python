# Dice

# This is very simple task to get you familiar with Unicode symbols and check how easy they can be used in Python.

# The task is to simulate a dice. You need to write a function that takes a number of throws and returns a string with needed random dices symbols separated by a space.

# Dices characters are: ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

# Examples of the correct work of the function dice():

# dice(1) # returns "⚃" (random values)
# dice(3) # returns "⚃ ⚁ ⚅" (random values)

# The following three constant definitions are equal.
# But the first(which looks the best) doesn't work
#   in CodeRunner
#DICES = "⚀⚁⚂⚃⚄⚅"  
#DICES = "\N{DIE FACE-1}\N{DIE FACE-2}\N{DIE FACE-3}" \
#        "\N{DIE FACE-4}\N{DIE FACE-5}\N{DIE FACE-6}"
import random

DICES = "\u2680\u2681\u2682\u2683\u2684\u2685"

def dice(number=1):
    return ' '.join(random.choice(DICES) for _ in range(number))

# Some basic tests
print(f'All dices are: {DICES}')
print(dice())  # Should output a random dice
print(dice(3))  # Should output 3 random dices separated by space
print(dice(3).count(" ") == 2 and len(dice(3)) == 5)  # Should be True
print(all(x in DICES for x in dice(3).replace(" ", "")))  # Should be True