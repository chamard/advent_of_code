# Get/Prepare data
with open("inputs.txt", 'r') as f:
    inputs = f.read()

data = [tuple(el.split(" ")) for el in inputs.splitlines()]


# part 1
rules = {
    ("A", "X"): 3 + 1,
    ("A", "Y"): 6 + 2,
    ("A", "Z"): 0 + 3,

    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3, 

    ("C", "X"): 6 + 1,
    ("C", "Y"): 0 + 2,
    ("C", "Z"): 3 + 3.
}
print(sum(map(lambda x: rules[x], data)))

# part 2
rules = {
    ("A", "X"): 0 + 3,
    ("A", "Y"): 3 + 1,
    ("A", "Z"): 6 + 2,

    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,

    ("C", "X"): 0 + 2,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 6 + 1.
}
print(sum(map(lambda x: rules[x], data)))

