import re
from utils.abstract import SolutionsAbstract


class SolutionsDay4(SolutionsAbstract):
    REQUIRED_ELEMENTS = {
        'eyr': r'^(202[0-9]|2030)$',
        'hgt': r'^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$',
        'iyr': r'^(201[0-9]|2020)$',
        'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
        'byr': r'^(19[2-9][0-9]|200[0-2])$',
        'hcl': r'^(#[a-z0-9]{6})$',
        'pid': r'^([0-9]{9})$',
    }

    @staticmethod
    def prepare_data(inputs):
        data = list()
        documents = re.split('\n\n', inputs)
        for document in documents:
            elements = re.split('\n| ', document)
            data.append(dict([re.split(':', element) for element in elements]))
        return data

    def part_1(self):
        required_elements = set(self.REQUIRED_ELEMENTS.keys())
        return len([1 for doc in self.data if set(doc.keys()).issuperset(required_elements)])

    def part_2(self):
        counter = 0
        for doc in self.data:
            match = all([re.match(regex, doc.get(element, '')) for element, regex in self.REQUIRED_ELEMENTS.items()])
            if match:
                counter += 1
        return counter
            
            
        
