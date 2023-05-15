# Simple reversing decorator

# The task is super simple - to write a simple decorator which will return result of decorated function but as a string and in reverse form.

# For example:

# @reverse
# def test_me():
#     return 25

# >>> test_me()
# "52"

def deco(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return str(result)[::-1]
    return wrapper

@deco
def test_me():
    return True
    
print(test_me())  # "eurT"