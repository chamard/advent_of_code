from functools import reduce
import operator
from utils.abstract import SolutionsAbstract


class SolutionsDay3(SolutionsAbstract):
    TREE = '#'
    SLOPS_PART_2 = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    @staticmethod
    def prepare_data(inputs):
        return inputs.splitlines()

    @classmethod
    def number_of_trees(cls, data, right, down):
        return len([1 for x, line in enumerate(data[0::down]) if line[x*right % len(line)] == cls.TREE])

    def part_1(self):
        return self.number_of_trees(self.data, 3, 1)

    def part_2(self):
        return reduce(operator.mul, [self.number_of_trees(self.data, *slop) for slop in self.SLOPS_PART_2])
