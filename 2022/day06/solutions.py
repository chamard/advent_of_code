# Get/Prepare data
with open("inputs.txt", 'r') as f:
    inputs = f.read()

# part 1
def find_distinct_character_position(inputs, number):
    data = [el for el in inputs]
    queue, data = data[:number], data[number:]
    while data and len(set(queue)) < number:
        queue.append(data.pop(0))
        queue.pop(0)
    return len(inputs) - len(data)

print(find_distinct_character_position(inputs, 4)) # 1134

# part 2
print(find_distinct_character_position(inputs, 14)) # 2263
