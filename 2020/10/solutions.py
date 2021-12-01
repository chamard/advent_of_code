from collections import defaultdict
from utils.abstract import SolutionsAbstract
    
class SolutionsDay10(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        data = set(map(int, inputs.splitlines()))
        return {0} | data | {max(data) + 3}
        
    def part_1(self):
        counter = {1:0, 2:0, 3:0}
        for el in self.data:
            for k in range(1, 4):
                if el + k in self.data:
                    counter[k] += 1
                    break
                            
        return counter[1] * counter[3]
            
    def part_2(self):
        data = sorted(self.data)
        arrangements = defaultdict(int)
        arrangements[0] = 1
        for i in range(1, len(data)):
            for j in range(1, min(i+1, 4)):
                if data[i] - data[i-j] <=3:
                    arrangements[i] += arrangements[i-j] 
        return arrangements[i]
