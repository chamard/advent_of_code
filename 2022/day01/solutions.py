# Get/Prepare data
with open("inputs.txt", 'r') as f:
    inputs = f.read()

data = [sum(map(int, elf.splitlines())) for elf in inputs.split("\n\n")]

# part 1
print(max(data)) #  71924

# part 2
print(sum(sorted(data)[-3:])) #  210406
