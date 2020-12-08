import re
from collections import defaultdict, namedtuple
from utils.abstract import SolutionsAbstract
    
Bags = namedtuple('Bags', ['number', 'bag_color'])

class SolutionsDay7(SolutionsAbstract):
    GOLD = 'shiny gold'
    
    @staticmethod
    def prepare_data(inputs):
        data_out, data_in = defaultdict(set), defaultdict(set)
        leaves_regex = re.compile(r'(\d+) (\w+ \w+)')
        
        for line in inputs.splitlines():
            node, leaves = re.split(' bags contain', line)
            leaves = leaves_regex.findall(leaves)
            for number, leaf in leaves:
                data_in[leaf].add(node)
                data_out[node].add(Bags(int(number), leaf))
                
        return {'in': data_in, 'out': data_out}

    def _get_unique_bags_contening(self, bag_color):
        bags = self.data['in'].get(bag_color, set())
        return set.union(bags, *[self._get_unique_bags_contening(in_bag) for in_bag in bags])
            
    def _count_bags_in(self, bag_color):
        bags = self.data['out'].get(bag_color, set())
        return sum([number * (self._count_bags_in(bags_color) + 1) for number, bags_color in bags])
        
    def part_1(self):
        return len(self._get_unique_bags_contening(self.GOLD))
        
    def part_2(self):
        return self._count_bags_in(self.GOLD)
