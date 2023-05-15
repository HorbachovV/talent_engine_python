# Anagram detection

# An anagram is the result of rearranging the letters of a word to produce a new word. Anagrams are case insensitive (meaning "AbC" and "acB" should be considered as anagrams).
# Examples:
# • foefet is an anagram of toffee • Buckethead is an anagram of DeathCubeK
# Task is to write a program which return boolean value ( True or False) based on are two passed string args are anagrams or not.

def is_anagram(str1: str, str2: str) -> bool:
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))
    

    return sorted_str1 == sorted_str2
    
print(is_anagram("AbbA", "BBaA"))