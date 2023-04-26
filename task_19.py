# Sum of digits in a string

# The task is write a function that return you a sum of all digits found in the strings.

# For example the sum of digits of the following string - "abc123___##05__5" is 1 + 2 + 3 + 0 + 5 + 5 = 16.

# The function received the string as the parameter and returns int result (if no digits - 0).

def sum_digits(input_str: str) -> int:
    digits = [int(char) for char in input_str if char.isdigit()]
    return sum(digits)
    
    
# Small tests
print(sum_digits("abc123___##05__5")) # 16
print(sum_digits("00000000000")) # 0
print(sum_digits("@@@@@@-1.0####")) # 1
print(sum_digits("100____½")) # 1