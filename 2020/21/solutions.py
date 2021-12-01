from collections import defaultdict
from utils.abstract import SolutionsAbstract
from typing import NamedTuple, List
import re
from collections import defaultdict
from functools import reduce


class SolutionsDay21(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        raw_data = list() 
        REGEX = re.compile(r'^(?P<ingredients>.*)\(contains (?P<allergens>.*?)\)')  
        for line in inputs.splitlines():
            d_line = REGEX.search(line).groupdict()
            raw_data.append(
                (
                    set(d_line['ingredients'].strip().split(' ')),
                    set(d_line['allergens'].strip().split(', ')) 
                )
            )

        all_ingredients = reduce(set.union, [el[0] for el in raw_data])
        all_allergens = reduce(set.union, [el[1] for el in raw_data])
        data = {allergens: all_ingredients.copy() for allergens in all_allergens}
        for ingredients, allergens in raw_data:
            for allergen in allergens:
                data[allergen].intersection_update(ingredients)

        return {
            'raw_data': raw_data,
            'data': data,
            'all_ingredients': all_ingredients,
            'all_allergens': all_allergens,
        }
                    
    def part_1(self):
        raw_data = self.data['raw_data']
        data = self.data['data']
        all_ingredients = self.data['all_ingredients']

        ingredients_that_may_contain_allergens = reduce(set.union, data.values())
        innert_ingredients = all_ingredients - ingredients_that_may_contain_allergens

        return sum([len(innert_ingredients.intersection(ingredients)) for ingredients, _ in raw_data])
    
    def part_2(self):
        data = self.data['data']
        all_allergens = self.data['all_allergens']
        deads = set()
        result = list()
        while len(result) != len(all_allergens):
            for k, v in data.items():
                if len(v - deads) == 1:
                    result.append((k, (v - deads).pop()))
                    deads.update(v)

        return ','.join([el[1 ]for el in sorted(result, key=lambda x: x[0])])
