# Narcissistic Number

# A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.
# For example, take 153 (3 digits):

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1634 (4 digits):

#     1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# The Challenge:
# Your code must return true or false depending upon whether the given number is a Narcissistic number.
# narcissistic(7)  # True,
# narcissistic(371) # True
# narcissistic(122) # False
# narcissistic(4887) # False

def narcissistic(test_number):
    num_str = str(test_number)
    
    n = len(num_str)
  
    sum_of_powers = sum(int(digit)**n for digit in num_str)

    if sum_of_powers == test_number:
        return True
    else:
        return False
    
    
print(narcissistic(7))  # True
print(narcissistic(371)) # True
print(narcissistic(122)) # False
print(narcissistic(4887)) # False