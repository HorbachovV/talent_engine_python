# Battery Capacity

# Task is to return the percent rated value of current battery capacity parsed from given string (let's assume it is some shell command's result).
# Current level should be calculated as CurrentCapacity / MaxCapacity in percents. The resulting value should be like the following example:
# 61.41%
# There are two ways:
# Parse from LegacyBatteryInfo block - this is super easy. If you are beginner - try to get needed info from this line.
# Parse from MaxCapacity/CurrentCapacity attributes - more complex task for more experienced programmers. If you want challenge - try to get information without using data from LegacyBatteryInfo block.
# The result of the function should be in the form of the string: "XX.YY%" where XX.YY is the float number of percents with 2 digits after dot.

import re

data = '''
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
'''

def get_battery_level(data):
    capacity_regex = r'"(?:CurrentCapacity|Capacity)"\s?=\s?(\d+);'
    legacy_regex = r'"LegacyBatteryInfo".*"Capacity"=(\d+),.*"Current"=(\d+),'
    
    # Search for capacity using MaxCapacity and CurrentCapacity
    capacity_match = re.search(capacity_regex, data)
    if capacity_match:
        max_capacity = int(capacity_match.group(1))
        current_capacity_match = re.search(r'"CurrentCapacity"\s?=\s?(\d+);', data)
        if current_capacity_match:
            current_capacity = int(current_capacity_match.group(1))
            level = (current_capacity / max_capacity) * 100
            return f"{level:.2f}%"

    # Search for capacity using LegacyBatteryInfo
    legacy_match = re.search(legacy_regex, data)
    if legacy_match:
        max_capacity = int(legacy_match.group(1))
        current_capacity = int(legacy_match.group(2))
        level = (current_capacity / max_capacity) * 100
        return f"{level:.2f}%"
    
    # If no capacity information found, return None
    return None

print(get_battery_level(data))