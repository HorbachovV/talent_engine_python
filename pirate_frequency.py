# Pirate frequency

# We need to count the frequency of each letter in a given string and return the sorted list with letters that appear more than a certain number of times.

# The function should receive two arguments:

# given string
# number of times the letter should be present
# The function returns:

# sorted list with letters that appear more than a given number of times
# Few examples:

# pirate_frequency("Ahoy, matey!", 1) # ['a', 'y'])
# pirate_frequency("Dead men tell no tales.", 3) # ["e"]
# pirate_frequency("Thar she blows!", 3) # []

from typing import List

def pirate_frequency(string: str, threshold: int) -> List[str]:
    """
    Returns a list of letters that appear more than a certain
    number of times in a given string.
    """
    freq = {}
    for char in string.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    result = []
    for letter, frequency in freq.items():
        if frequency > threshold:
            result.append(letter)

    return sorted(result)

print(pirate_frequency("Ahoy, matey!", 1)) #['a', 'e', 'o', 'y'])