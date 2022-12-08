# Get/Prepare data
with open('inputs.txt', 'r') as f:
    inputs = f.read()

map_trees = [list(map(int, line)) for line in inputs.splitlines()]

def print_trees(map_trees):
    size = len(map_trees[0])
    print(" . | " + " ".join(map(str, range(size))))
    print(" _ | " + "_ " * size)
    for i, row in enumerate(map_trees):
        print(f" {i} | " + " ".join(map(str, row)))

# part 1
nb_visible, max_score = 0, 0
for y, row in enumerate(map_trees):
    for x, tree in enumerate(row):
        right = map_trees[y][:x][::-1]
        left = map_trees[y][x+1:]
        top = [map_trees[i][x] for i in range(y)][::-1]
        bellow =  [map_trees[i][x] for i in range(y+1, len(row))]

        # part 1
        for direction in (right, left, top, bellow):
            if not direction or tree > max(direction):
                nb_visible += 1
                break
        
        # part 2
        score = 1
        for direction in (right, left, top, bellow):
            try:
                score *= list(d >= tree for d in direction).index(True) + 1
            except ValueError:
                score *= len(direction)

        max_score = max(max_score, score)
        
# part 1
print(nb_visible)
        
# part 2
print(max_score)
