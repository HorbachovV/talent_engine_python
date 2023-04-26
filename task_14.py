# Balanced List

# The task is to write a function which should generate a list with integers that in sum will give zero.

# For example, num is 3 and 5:

# gen_list(3)  # [1, 2, -3]
# gen_list(5)  # [1, 2, 3, 4, -10]

def gen_list(num=3):
    res = list(range(1, num))
    res.append(-sum(res))
    return res
    
print(gen_list(5))