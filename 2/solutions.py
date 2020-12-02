import re
from collections import Counter

def get_data():
    REGEX = re.compile(r'^(?P<val_1>\d+)-(?P<val_2>\d+) (?P<char>\w): (?P<password>.*)$')
    data = list()
    with open('inputs.txt') as f:
        for line in f:
            data.append(REGEX.search(line).groupdict())
    return data

def part_1(data):
    counter = 0
    for d in data:
        c = Counter(d['password'])
        if  int(d['val_1']) <= c[d['char']] <= int(d['val_2']):
            counter += 1
    return counter

def part_2(data):
    counter = 0
    for d in data:
        pwd = d['password']
        idx_1 = int(d['val_1']) - 1
        idx_2 = int(d['val_2']) - 1
        assert max(idx_1, idx_2) < len(pwd), 'index out of range'
        nb_match = len([idx for idx in [idx_1, idx_2] if pwd[idx] == d['char']])
        if nb_match == 1:
            counter += 1
    return counter

def main():
    data = get_data()
    print(f'Solution part 1: {part_1(data)}') # 569
    print(f'Solution part 2: {part_2(data)}') # 346

if __name__ == '__main__':
    main()
