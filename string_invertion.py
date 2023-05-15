# String invertion

# Write three methods of string invertion.
# s = "Invert me please"
# You need to get "esaelp em trevnI" in a three different ways

string_ = "Revert me please:)"

def method_1(string_):
    inverted_s = ''.join(reversed(string_))
    return inverted_s
    
def method_2(string_):
    inverted_s = ''
    for i in range(len(string_)-1, -1, -1):
        inverted_s += string_[i]
    return inverted_s
    
def method_3(string_):
    inverted_s = ''.join([string_[i] for i in range(len(string_)-1, -1, -1)])
    return inverted_s
    
print("1 -->", method_1(string_))
print("2 -->", method_2(string_))
print("3 -->", method_3(string_))