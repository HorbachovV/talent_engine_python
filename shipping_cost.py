# Shipping Cost

# Here you need to write a helpful tool for a shipping company to calculate the cost of shipping cargo based on its weight and destination port.

# Shipping rates are predefined (shipping_rates dict with destination and the cost for 1 weight entity of cargo).

# Each cargo item is defined with a tuple in a form: (<name>, <weight>, <destination>).

# Create a function that takes a list of cargo items and string for specific port and calculates the total shipping cost for all items that are being shipped to that specific port. The function should return the total cost as a floating point number.

# For example the following should return 900.0:

# calculate_total_cost_to_port([("Apples", 5.0, "New York"), ("Oranges", 3.0, "Los Angeles"), ("Bananas", 2.5, "Seattle"), ("Pineapples", 4.0, "Houston")], "Los Angeles") #     900.0
# because we have only ("Oranges", 3.0, "Los Angeles") for Los Angeles and as the rate for this port is 300.0 (see default solution header as shipping_rates are defined there) 3 * 300.0 = 900.0.

from typing import List, Tuple

shipping_rates = {
    'New York': 250.0,
    'Los Angeles': 300.0,
    'Seattle': 200.0,
    'Houston': 275.0
}


def total_cost_to_port(cargo: List[Tuple[str, float, str]], port: str) -> float:
    """The function calculates the total shipping cost
    for all items that are being shipped to that specific port.
    """
    total_cost = 0.0
    rate = shipping_rates.get(port)
    if rate is not None:
        for item in cargo:
            name, weight, destination = item
            if destination == port:
                total_cost += weight * rate
    return total_cost