# Give me numbers!

# Please write a program which will find numbers (integers) which are divisible by 7 and 13 but are not a multiple of 5. They should be between 333 and 7553 (both included).
# Sample:
# 364
# 546
# 637
# 728
# They all are divisable by 7 and 13 but not by 5:
# 364 / 7 = 52
# 364 / 13 = 28
# 364 / 5 = 72.8
# You should return a list of needed numbers:
# [364, 546, 637, 728, ... , ]

def test_me(x=333, y=7553):
    result = []
    for i in range(333, 7554):
        if i % 7 == 0 and i % 13 == 0 and i % 5 != 0:
            result.append(i)
    return result

print(test_me())