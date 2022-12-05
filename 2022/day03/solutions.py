# Get/Prepare data
with open("inputs.txt", 'r') as f:
    inputs = f.read()

data = inputs.splitlines()

# part 1
types = list()
for el in data:
    mid = int(len(el) / 2)
    types.append(set(el[:mid]).intersection(el[mid:]).pop())

get_priority = lambda x:ord(x.upper()) - ord("A") +1 + {True:26, False: 0}[x.isupper()]
print(sum(map(get_priority, types)))

# part 2
badges = []
for i in range(int(len(data)/3)):
    a, b, c = data[i * 3: i * 3 +3]
    badges.append(set(a).intersection(b).intersection(c).pop())

print(sum(map(get_priority, badges)))
