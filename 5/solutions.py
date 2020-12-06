from utils.abstract import SolutionsAbstract


class SolutionsDay5(SolutionsAbstract):
    code_to_binary = {
        'F': '0',
        'B': '1',
        'L': '0',
        'R': '1',
    }
    
    @staticmethod
    def prepare_data(inputs):
        return inputs.splitlines()
    
    @classmethod
    def _code_to_int(cls, code):
        return int(''.join([cls.code_to_binary[el] for el in code]), 2)

    def part_1(self):
        return max(map(self._code_to_int, self.data))

    def part_2(self):
        seats = set(map(self._code_to_int, self.data))
        for seat in seats:
            if all([seat + 1 not in seats, seat + 2 in seats]):
                return seat + 1
