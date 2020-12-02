from functools import reduce
import operator

def get_data():
    data = set()
    with open('inputs.txt') as f:
        for line in f:
            data.add(int(line))
    return data

def find_pair(target, data):
    data_map = {d: True for d in data}
    for a in data:
        b = target - a
        if data_map.get(b):
            return a, b

def find_triple(target, data):
    for a in data:
        pair = find_pair(target - a, data - set([a]))
        if pair:
            return a, *pair

def main():
    target = 2020
    data = get_data()

    part_1 = reduce(operator.mul, find_pair(target, data))
    print(f'Solution part 1: {part_1}') # 921504

    part_2 = reduce(operator.mul, find_triple(target, data))
    print(f'Solution part 2: {part_2}') # 195700142


if __name__ == '__main__':
    main()
