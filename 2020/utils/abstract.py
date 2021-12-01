from pathlib import Path, PurePath
import inspect

class SolutionsAbstract:

    def __init__(self):
        self.inputs = self._get_inputs()
        self.data = self.prepare_data(self.inputs)

    @property
    def input_path(self):
        base_path = Path(inspect.getmodule(self).__file__).parent
        return PurePath.joinpath(base_path, 'inputs.txt')

    def _get_inputs(self):
        with open(self.input_path, 'r') as f:
            inputs = f.read()
        return inputs

    @staticmethod
    def prepare_data(inputs):
        return inputs

    def part_1(self):
        pass

    def part_2(self):
        pass

    def print_solutions(self):
        print(f'Solution part 1: {self.part_1()}')
        print(f'Solution part 2: {self.part_2()}')
