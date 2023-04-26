# Bird Sightings

# Write a function that takes a list of bird sightings, where each sighting is represented as a tuple of the form: (<species>, <color>) and returns a dictionary that maps each color to the most commonly observed bird species of that color. If there are multiple species that are equally common for a given color, the function should return any one of those species.

# For example these are sample sightings:

# [
#     ("Robin", "red"),
#     ("Sparrow", "brown"),
#     ("Robin", "brown"),
#     ("Blue Jay", "blue"),
#     ("Sparrow", "brown"),
#     ("Blue Jay", "blue"),
#     ("Sparrow", "blue"),
#     ("Sparrow", "brown")
# ]
# We can see that there is 1 red birds (Robin), 4 brown birds (3 Sparrow and 1 Robin), 3 blue bird (2 Blue Jays and 1 Sparrow).

# For such input the function should return:

# {'red': 'Robin', 'brown': 'Sparrow', 'blue': 'Blue Jay'})

from typing import List, Tuple, Dict
from collections import defaultdict

def analyze_birds(sightings: List[Tuple[str, str]]) -> Dict[str, str]:
    """
    Returns a dictionary that maps each color to the most commonly observed bird species of that color.
    If there are multiple species that are equally common for a given color, returns any one of those species.
    """
    color_to_species = defaultdict(list)
    for species, color in sightings:
        color_to_species[color].append(species)
    
    result = {}
    for color, species_list in color_to_species.items():
        species_counts = defaultdict(int)
        for species in species_list:
            species_counts[species] += 1
        
        most_common_species = None
        most_common_count = -1
        for species, count in species_counts.items():
            if count > most_common_count:
                most_common_species = species
                most_common_count = count
        
        result[color] = most_common_species
    
    return result
    
    
# Should return: {'red': 'Robin', 'brown': 'Sparrow', 'blue': 'Blue Jay'})    
print(analyze_birds([("Robin", "red"), ("Sparrow", "brown"), ("Robin", "brown"), ("Blue Jay", "blue"), ("Sparrow", "brown"), ("Blue Jay", "blue"), ("Sparrow", "blue"), ("Sparrow", "brown")]))
               