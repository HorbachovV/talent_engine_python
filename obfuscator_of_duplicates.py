# Obfuscator of duplicates

# Being given a string with some random characters you need to change all 3-in-a-row duplicated characters (case insensitive) with "***" substring.

# Example string:

# "AaA some random text bla bla bla BBB CCCC boom shakalaka!"
# should be changed to:

# "*** some random text bla bla bla *** ***C boom shakalaka!"
# Some hints/recommendations/examples:

# It is possible to do this task without regular expression - using just for cycle
# To use group inside regular expression use \1, \2 etc. like
# re.search(r"(\w+), where are you, \1?", "Tom, where are you, Tom?").group(1) ---> "Tom"
# re.sub() can be used to replace findings with replacement string (or result of given function)
# re.findall() will return a list with groups if regular expression was using them so here probably you'll want to use re.finditer or re.sub
# re.finditer() is returning iterator which gives out found matches, please test this:
# for match in re.finditer(r'(?i)(\w+) is \1', 'Deal is deal, good is bad, sun is sun...'):
#     print(match.group(1)) # ---> "Deal", "sun"

test_string = "Hello, my password is: 'AaaBBBccc', cooool, right?"
expected_result = "Hello, my password is: '*********', c***ol, right?"

def test_me(test_string):
    # do something!
    import re
    pattern = r"(?i)(\w)\1\1"
    result = re.sub(pattern, "***", test_string)
    return result

if test_me(test_string) == expected_result:
    print("You did well: %s" % expected_result)
else:
    print("You got:\n%s\nTry again..." % test_me(test_string))