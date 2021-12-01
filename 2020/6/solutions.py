import re
from functools import reduce
import copy
from utils.abstract import SolutionsAbstract


class SolutionsDay6(SolutionsAbstract):
    
    @staticmethod
    def prepare_data(inputs):
        documents = re.split('\n\n', inputs)
        return [map(set, doc.splitlines()) for doc in documents]

    def _sum_reduce(self, operator):
        data = copy.deepcopy(self.data)
        return sum([len(reduce(operator, el)) for el in data])

    def part_1(self):
        return self._sum_reduce(set.union)

    def part_2(self):
        return self._sum_reduce(set.intersection)
