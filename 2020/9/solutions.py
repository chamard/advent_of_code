from utils.abstract import SolutionsAbstract
    
class SolutionsDay9(SolutionsAbstract):
    preamble = 25
     
    @staticmethod
    def prepare_data(inputs):
        return list(map(int, inputs.splitlines()))
    
    @staticmethod
    def _is_sum_of(data, el):
        return [1 for d in set(data) if el - d in data]
        
    def part_1(self):
        for i, el in enumerate(self.data[self.preamble::]):
            if not self._is_sum_of(self.data[i : i+ self.preamble], el):
                return el
    
    def part_2(self):
        a ,b = 0, 1
        invalid_number = self.part_1()
        last_indice = len(self.data)
        sum_ = sum([self.data[a], self.data[b]])
        while a < last_indice - 1:
            if sum_ < invalid_number:
                b +=1
                sum_ += self.data[b]
            elif sum_ > invalid_number:
                sum_ -= self.data[a]
                a +=1
            else:
                contiguous_set = self.data[a:b]
                return sum([min(contiguous_set), max(contiguous_set)])
