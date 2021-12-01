from utils.abstract import SolutionsAbstract
from collections import defaultdict
import re
    
class SolutionsDay14(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        REGEX = re.compile(r'mem\[(\d+)\] = (\d+)')
        masks = defaultdict(list)
        for line in inputs.splitlines():
            if 'mask ='  in line:
                 mask = line.split()[2]
            else:
                masks[mask].append(REGEX.match(line).groups())
        return masks

    def do_shit(self, mask, value):
        r = list()
        bin_value = bin(value)[2:]
        bin_value = '0'*(36-len(bin_value)) + bin_value
        for m, v in zip(mask, bin_value):
            if m == 'X':
                r.append(v)
            else:
                r.append(m)
        
        return int(''.join(r), 2)

    def part_1(self):
        mem = dict()
        for mask, values in self.data.items():
            for value in values:
                mem[value[0]] = self.do_shit(mask, int(value[1]))

        return sum(mem.values())
        
    def part_2(self):
        pass
