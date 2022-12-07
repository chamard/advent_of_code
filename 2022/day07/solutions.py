from collections import defaultdict

# Get/Prepare data
with open('inputs.txt', 'r') as f:
    inputs = f.read()


# part 1
executions = (inputs.split('$ '))[1:]
path_to_size, position= {}, []

for execution in executions:
    command, *output = execution.splitlines()
    program, *args = command.split(' ')
    if program == "cd":
        match move_to:=args[0]:
            case "/":
                position = [move_to]
            case "..":
                position.pop()
            case _:
                position.append(move_to)
    elif program == 'ls':
        for line in output:
            size, name = line.split(' ')
            if size != 'dir':
                path_to_size[tuple(position) + (name,)] = int(size)

sizes = defaultdict(int)
for path, size in path_to_size.items():
    position = []
    for p in path:
        sizes[tuple(position)] += size
        position.append(p)

print(sum([size for size in sizes.values() if size <= 100_000])) # 1447046

# part 2
size_total = 70_000_000
size_required = 30_000_000
size_taken = sizes[("/")]

print(max(size for size in sizes.values() if size_total - (size_taken - size) >= size_required)) # 40572957