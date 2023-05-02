# Polish Flag

# The task is to create a function to return a string containing Polish flag formatted from the lines created using unicode symbols - "White Large Square" and "Red Large Square".

# An example:

# flag(8, 4)  # width = 8, height = 4

# ⬜⬜⬜⬜⬜⬜⬜⬜
# ⬜⬜⬜⬜⬜⬜⬜⬜
# 🟥🟥🟥🟥🟥🟥🟥🟥
# 🟥🟥🟥🟥🟥🟥🟥🟥
# The function flag() receives two parameters - width and height of the flag.

# Characters to use (in order to use in Training Suite runner):

# "\u2B1c" - White Large Square (⬜)
# "\U0001F7E5" - Red Large Square (🟥)
# NOTE: The function should return a string, so please avoid using print() inside it. You need to print out the result of the function instead, see the default code as the template.

def flag(width=10, height=4):
    result = ""
    for row in range(height):
        for col in range(width):
            if row < height//2:
                # white row
                result += "\u2B1c"
            else:
                # red row
                result += "\U0001F7E5"
        # end of row
        result += "\n"
    return result
    
print(flag())