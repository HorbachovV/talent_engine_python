# Palindrome detection

# Anagrams are easy, now let's play with palindrome!

# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
# The task is to check is this string a palindrome or not (return True/False)

# Ignore case (case-insensitive: "Madam" should be considered as palindrome)
# Ignore spaces ("Race Car" should be considered as palindrome)
# Ignore punctuation ("A man, a plan, a canal, Panama!" is palindrome too)

import string

def is_palindrome(s):
    s = s.lower()
    s = s.translate(str.maketrans("", "", string.punctuation))
    s = s.replace(" ", "")
    
    return s == s[::-1]
    
print(is_palindrome("racecar")) # True
print(is_palindrome("Race Car")) # True
print(is_palindrome("A man, a plan, a canal, Panama!"))  # True