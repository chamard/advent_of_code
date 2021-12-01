from functools import reduce
import operator
from utils.abstract import SolutionsAbstract

def find_pair(target, data):
    for a in data:
        b = target - a
        if b in data:
            return a, b

def find_triple(target, data):
    for a in data:
        pair = find_pair(target - a, data - set([a]))
        if pair:
            return (a, *pair)


class SolutionsDay1(SolutionsAbstract):
    TARGET = 2020

    @staticmethod
    def prepare_data(inputs):
        return set(map(int, inputs.splitlines()))

    def part_1(self):
        return reduce(operator.mul, find_pair(self.TARGET, self.data))

    def part_2(self):
        return reduce(operator.mul, find_triple(self.TARGET, self.data))
