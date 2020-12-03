import re
from collections import Counter
from utils.abstract import SolutionsAbstract


class SolutionsDay2(SolutionsAbstract):

    @staticmethod
    def prepare_data(inputs):
        REGEX = re.compile(r'^(?P<val_1>\d+)-(?P<val_2>\d+) (?P<char>\w): (?P<password>.*)$')
        return [REGEX.search(line).groupdict() for line in inputs.splitlines()]

    def part_1(self):
        counter = 0
        for d in self.data:
            c = Counter(d['password'])
            if  int(d['val_1']) <= c[d['char']] <= int(d['val_2']):
                counter += 1
        return counter

    def part_2(self):
        counter = 0
        for d in self.data:
            pwd = d['password']
            idx_1 = int(d['val_1']) - 1
            idx_2 = int(d['val_2']) - 1
            assert max(idx_1, idx_2) < len(pwd), 'index out of range'
            nb_match = len([idx for idx in [idx_1, idx_2] if pwd[idx] == d['char']])
            if nb_match == 1:
                counter += 1
        return counter
