from functools import reduce
import operator

TREE = '#'

def get_data():
    data = list()
    with open('inputs.txt') as f:
        for line in f:
            data.append(line.strip())
    return data

def number_of_tree(data, right, down):
    return len([1 for x, line in enumerate(data[0::down]) if line[x*right % len(line)] == TREE])

def main():
    data = get_data()
    print(f'Solution part 1: {number_of_tree(data, 3, 1)}') # 569

    slops = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
        ]

    part_2 = reduce(operator.mul, [number_of_tree(data, *slop) for slop in slops])
    print(f'Solution part 2: {part_2}') # 346

if __name__ == '__main__':
    main()
