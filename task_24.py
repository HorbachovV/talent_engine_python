# Common Topics

# Task is to help a few friends to talk... Each of them has his own own interests which presented as strings in list. Please find three most common topics to talk based on given list of friends.

# Example (3 friends):

# friends = [
#   ["Python", "Drawing", "Music", "Games", "Girls"],
#   ["Aerobics", "Politics", "Books", "Girls", "Python"],
#   ["Cinema", "Music", "Drawing", "Python", "Books", "Games"]
# ]
# You should get:

# ["Python", "Books", "Drawing"]
# Because "Python" is encountered 3 times - most popular topic. "Books", "Music", "Drawing", "Girls" and "Games" are encountered 2 times each but as only 3 topics needed in total - so you should return needed number of same-tier values by sorting them as strings.

# Please note that a single entry form the one person should be counted. All duplicated ones in a single list should be ignored. In other words ["Games", "Games", "Python"] should be treated the same as ["Games", "Python"].

# P.S. Sorted list of 2-numbered topics:

# ["Books", "Drawing", "Games", "Girls", "Music"][:2]  # -->  ["Books", "Drawing"]

FRIENDS = [
  ["Python", "Drawing", "Games", "Girls", "Weapons", "Games", "Books"],
  ["Music", "Politics", "Books", "Girls", "Python", "Cinema", "Cars"],
  ["Cinema", "Music", "Drawing", "Python", "Books", "History"],
  ["War", "Sport", "Books", "Games", "Python", "Cinema", "Cars"],
  ["Knifes", "Games", "Books", "Girls", "Cinema", "Cars", "Python"],
  ["Sport", "Drawing", "Books", "Girls", "Games",  "Music"],
]


def get_common_topics(friends=FRIENDS, topics=3):
    topics_dict = {}
    for friend in friends:
        friend_set = set(friend)
        for topic in friend_set:
            if topic in topics_dict:
                topics_dict[topic] += 1
            else:
                topics_dict[topic] = 1
    
    sorted_topics = sorted(topics_dict.items(), key=lambda x: (-x[1], x[0]))
    result = [sorted_topics[i][0] for i in range(topics)]
    return result


print(get_common_topics())