# Find longest palindrome

# Palindrome is the sequence of characters which reads the same backward as forward, such as madam or racecar or the number 10801.

# The task is to find the longest palindrome that contained in the given string.

# For example, the string "AbAtopot123321" has 3 different palindromes: "AbA", "topot" and "123321". Obviously, the last one is the longest.

# The function get_longest_palindrome should take 1 argument - given string and return the string which is the longest palindrome inside the given string.

def get_longest_palindrome(s):
    longest_palindrome = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    
    return longest_palindrome
    
    
print(get_longest_palindrome("AbAtopot123321")) # 123321
                                    