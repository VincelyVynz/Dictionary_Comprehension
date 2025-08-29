# ---------------------------- Dictionary Comprehension ---------------------------- #

"""

Used to create a new dictionary by shortening a for loop.

Syntax:

    newdict = {key_expr: value_expr for item in iterable if condition == True}

"""


new_dict = {
    "name": "Alice",
    "age": 22,
    "city": "New York",
    "state": "NY",
    "country": "USA"
}

inverted_dict = { v:k for k, v in new_dict.items() }

print(inverted_dict)


# Creating a dictionary from two lists:
