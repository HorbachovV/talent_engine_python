# GCD

# Write a function to return GCD (Greatest Common Divisor) of two integers.

# Greatest common divisor (gcd) of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder. For example, the GCD of 8 and 12 is 4.
# Example:

# >>> gcd(8, 12)
# 4

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(gcd(8, 12))
print(gcd(54, 24))