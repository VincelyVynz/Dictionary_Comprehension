# ---------------------------- Dictionary Comprehension ---------------------------- #

# importing pprint to print dictionaries in a readable way
from pprint import pprint

"""

Used to create a new dictionary by shortening a for loop.

Syntax:

    newdict = {key_expr: value_expr for item in iterable if condition == True}


To invert a dictionary:

    original = {'a': 1, 'b': 2}
    inverted = {v: k for k, v in original.items()}

    k - key
    v - value

"""


new_dict = {
    "name": "Alice",
    "age": 22,
    "city": "New York",
    "state": "NY",
    "country": "USA"
}

inverted_dict = { v:k for k, v in new_dict.items() }

pprint(inverted_dict)

# Creating a dictionary from two lists:

titles = ["name", "age", "city", "state", "country"]

alice = ["Alice", 22, "New York", "NY", "USA"]

alice_dict = {k : v for k, v in zip(titles, alice)}

# Shorter way to do the same:
# alice_dict = dict(zip(titles, alice)

pprint(alice_dict)

#dictionary comprehension with if statement

alice_dict_str = { k:v for k, v in zip(titles, alice) if type(v) is str}
# Checking each v because the list-alice has both str and int, and type(alice) != str and will return nothing [type(alice) checks the whole list]

pprint(alice_dict_str)


# cartesian dict
list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = [1,2,3,4,5]

cartesian_dict = {f"{x.upper()}{y}": (x, y) for x in list_1 for y in list_2}

pprint(cartesian_dict)