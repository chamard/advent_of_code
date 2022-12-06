import re

# Get/Prepare data
with open("inputs.txt", 'r') as f:
    inputs = f.read()

REGEX = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
data = [list(map(int, REGEX.search(x).groups())) for x in inputs.splitlines()]

fully_included_count = 0 
overlap_count = 0
for a, b, c, d in data:
    ab = set(range(a, b +1))
    cd = set(range(c, d +1))
    intersection = ab.intersection(cd)
    if len(intersection) == len(ab) or len(intersection) == len(cd):
        fully_included_count += 1
    if intersection:
        overlap_count += 1

# Part 1
print(fully_included_count) #  413

# Part 2
print(overlap_count) #  806
