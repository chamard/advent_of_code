import re

# Get/Prepare data
initial_stacks = {
    1: ["V", "C", "D", "R", "Z", "G", "B", "W"],
    2: ["G", "W", "F", "C", "B", "S", "T", "V"],
    3: ["C", "B", "S", "N", "W"],
    4: ["Q", "G", "M", "N", "J", "V", "C", "P"],
    5: ["T", "S", "L", "F", "D", "H", "B"],
    6: ["J", "V", "T", "W", "M", "N"],
    7: ["P", "F", "L", "C", "S", "T", "G"],
    8: ["B", "D", "Z"],
    9: ["M", "N", "Z", "W"],
}

with open("inputs.txt", 'r') as f:
    inputs = f.read()

REGEX = re.compile(r"move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)")
instructions = list(
    map(
        lambda x: list(map(int, REGEX.search(x).groups())),
        inputs.splitlines()[10:]
    )
)

# part 1
def get_code(stack, instructions, side):
    for move, from_stack_id, to_stack_id in instructions:
        stack[from_stack_id], temp = stack[from_stack_id][:-move], stack[from_stack_id][-move:]
        stack[to_stack_id].extend(temp[::side])
    return ''.join([v[-1] for k, v in stack.items()])

print(get_code(initial_stacks.copy(), instructions, -1)) # TBVFVDZPN

# part 2
print(get_code(initial_stacks.copy(), instructions, 1)) # VLCWHTDSZ
