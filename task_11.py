#  Group Anagrams

# Task is to process all words from input sequence and return a list with lists from those words that are anagrams with others in their list

# A typical test could be :

# list_ = ["tsar", "rat", "tar", "star", "tars", "cheese"]
# group_anagrams(list_)  # [["tsar", "star", "tars"], ["rat", "tar"], ["cheese"]]
# NOTE: the order of words in resulted lists should follow the order of appearance.

test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]

def group_anagrams(test_list):
    groups = {}
    for word in test_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]
    return [v for k, v in groups.items()]


print(group_anagrams(test_list))
                                    
                                    