# Unused Digits

# Given few numbers, you need to return the digits that are not being used.

# An examples:

# unused_digits(12, 34, 56, 78) # "09"
# unused_digits(2015, 8, 26) # "3479"

def unused_digits(*args):
    all_digits = set("0123456789")
    used_digits = set(digit for num in args for digit in str(num))
    unused_digits = all_digits - used_digits
    return "".join(sorted(unused_digits))
    
print(unused_digits(12, 34, 56, 78)) # "09"
print(unused_digits(2015, 8, 26)) # "3479"