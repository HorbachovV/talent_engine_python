# Tribonacci

# Tribonacci number works basically like a Fibonacci number with only difference that we should sum the last 3 (instead of 2) numbers of the sequence to generate the next item.

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1, 1, 3, 5, 9, 17, 31, ... ]
# If we started with [0, 0, 1] as a signature:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ... ]
# Task is to write tribonacci function which will generate sequence of numbers of given length as function's integer argument and given signature as sequence of three integers.

def tribonacci(length=8, signature=(0, 1, 1)):
    
    result = list(signature)

    while len(result) < length:
        
        next_num = sum(result[-3:])
        result.append(next_num)

    return result