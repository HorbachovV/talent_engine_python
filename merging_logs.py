# Merging logs

# You have two list of dictionaries of this format:

# {"id": "123123123123123", "message": "Some logged message", "datetime": 1474624791}
# You need to merge two list removing possible duplicates (judging by id key of dicts)

# And additionally - sort resulted list by datetime timestamp(UNIX seconds).

list1 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "123124", "message": "DB stopped! Whatta hell!", "datetime": 1474456391},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "1223134", "message": "U hev bin pwned by hax0r tim!", "datetime": 1474624799},
    {"id": "1213234", "message": "Need more vespene gas!", "datetime": 1474624791},
]

list2 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "3334113", "message": ""'; DELETE FROM customers WHERE 1 or username = '"; ", "datetime": 1474624789},
    {"id": "1213235", "message": "Require more minerals!", "datetime": 1474624792},
]

def merge_logs(list1, list2):
    merged = list1 + list2  # Combine the two lists
    
    # Remove duplicates based on 'id' key
    merged = {item['id']: item for item in merged}.values()
    
    # Sort the merged list by 'datetime' timestamp
    sorted_logs = sorted(merged, key=lambda x: x['datetime'])
    
    return sorted_logs

print(merge_logs(list1, list2))
                                   