import re
import copy
from collections import defaultdict
from utils.abstract import SolutionsAbstract
from dataclasses import dataclass

@dataclass
class Line:
    instruction: str
    argument: int
    
    def flip(self):
        self.instruction = {'jmp': 'nop', 'nop': 'jmp'}[self.instruction]
    
class SolutionsDay8(SolutionsAbstract):
    actions = {
        'acc': lambda x: (x, 1),
        'jmp': lambda x: (0, x), 
        'nop': lambda x: (0, 1),
    }
    
    @staticmethod
    def prepare_data(inputs):
        data = dict()
        for idx, line in enumerate(inputs.splitlines()):
            instruction, argument = re.split(' ', line)
            data[idx] = Line(instruction, int(argument))
        return data
    
    def _get_next(self, data, acc, idx):
        line = data[idx]
        del data[idx] # dict.pop is evil. Never use it.
        acc_change, idx_change = self.actions[line.instruction](line.argument)
        acc += acc_change
        idx += idx_change
        return  data, acc, idx 
        
    def get_acc_if_occurance(self, data, acc, idx):
        data, acc, idx = self._get_next(data, acc, idx)
        return self.get_acc_if_occurance(data, acc, idx) if idx in data else acc
    
    def get_acc_if_terminated(self, data, acc, idx):
        data, acc, idx = self._get_next(data, acc, idx)
        if idx > max(data.keys()):
            return acc
        elif idx in data:
            return self.get_acc_if_terminated(data, acc, idx)

    def get_part_2(self, data, acc, idx):
        data, acc, idx = self._get_next(data, acc, idx)
        if data[idx].instruction in ['jmp', 'nod']:
            data_c = copy.deepcopy(data)
            data_c[idx].flip()
            final_acc = self.get_acc_if_terminated(data_c, acc, idx)
            if final_acc:
                return final_acc
        return self.get_part_2( data, acc, idx)

    def part_1(self):
        data = copy.deepcopy(self.data)
        return self.get_acc_if_occurance(data, 0, 0)

    def part_2(self):
        data = copy.deepcopy(self.data)
        return self.get_part_2(data, 0, 0)
