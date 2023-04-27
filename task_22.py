# Resources Check

# Here we will be helping architects/builders to check is the existing resources are enough for the building they are planning to work on.

# You will have existing storage with all existing resources that building company current has:

# storage = {
#     'wood': 100,
#     'stone': 50,
#     'bricks': 200,
#     'glass': 20
# }
# The task is to write a function to check are resources are enough for the task.

# The function should receive the list of tuples, each tuple contains the name of required resource and it's required quantity. The function should return boolean value.

# This example will return True:

# has_enough_resources([("wood", 50), ("stone", 20), ("bricks", 100), ("glass", 20)])

# because mentioned resources quantities are less or equal than than existing ones in storage.

# This example will return False:

# has_enough_resources([("wood", 150), ("stone", 20), ("bricks", 50), ("glass", 20)])

# because there is not enough wood in the storage (required 150 > existing 100).

from typing import List, Tuple

storage = {
    'wood': 100,
    'stone': 50,
    'bricks': 200,
    'glass': 30
}

def has_enough_resources(required_resources: List[Tuple[str, int]]) -> bool:
    for resource, quantity in required_resources:
        if resource not in storage or quantity > storage[resource]:
            return False
    return True


print(has_enough_resources([("wood", 50), ("stone", 20), ("bricks", 100), ("glass", 20)])) # True
print(has_enough_resources([("wood", 150), ("stone", 20), ("bricks", 50), ("glass", 20)])) # False