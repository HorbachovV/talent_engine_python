# Rabbits and chickens

# Let's count animals on a farm!

# The farm contains rabbits and chickens. We know counts of heads and legs and need to get the number of rabbits (they have 1 head and 4 legs each!) and the number of chickens (1 head + 2 legs).

# For example, we have 3 heads and 10 legs. By brute-force, we should get 2 rabbits and 1 chicken.

# The function should receive heads and legs and return numbers for rabbits and chickens or return the string "Not possible".

def count_rabbits_chickens(heads, legs):
    max_rabbits = legs // 4
    
    for num_rabbits in range(max_rabbits+1):

        remaining_legs = legs - num_rabbits * 4
        
        num_chickens = remaining_legs // 2
        
        if num_rabbits + num_chickens == heads:
            return num_rabbits, num_chickens
    
    return "Not possible"
    
    
print(count_rabbits_chickens(3, 10))  # 2, 1