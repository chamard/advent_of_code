from collections import defaultdict
from utils.abstract import SolutionsAbstract
from typing import NamedTuple
import copy

class Coord(NamedTuple):
    x: int
    y: int
    
    def get_with_offset(self, x, y):
        return self.__class__(self.x + x, self.y +y)
    
class SolutionsDay11(SolutionsAbstract):
    OCCUPIED = '#'
    FLOOR = '.'
    EMPTY = 'L'
    DIRECTIONS = {(0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, -1)}
     
    @staticmethod
    def prepare_data(inputs):
        return {
            Coord(x, y): c
            for x, line in enumerate(inputs.splitlines())
            for y, c in enumerate(line)
        } # {Coord(0,0): 'L', Coord(0,1): 'X', ... }
    
    @classmethod
    def count_occupied(cls, coord, data, ignore_type=None):
        occ = 0
        for x, y in cls.DIRECTIONS:
            while ignore_type and data.get(coord.get_with_offset(x, y)) == ignore_type:
                x , y = cls.increment_direction(x), cls.increment_direction(y)
            if data.get(coord.get_with_offset(x, y)) == cls.OCCUPIED:
                occ += 1
        return occ 
    
    @classmethod
    def increment_direction(cls, i):
        if i == 0:
            return 0
        elif i > 0:
            return i + 1
        else:
            return i - 1
        
    @classmethod    
    def update_seats(cls, data, limit, ignore_type=None):
        new_data = data.copy()
        for coord, spot in data.items():
            if spot == cls.FLOOR:
                continue
                         
            nb_occupied = cls.count_occupied(coord, data, ignore_type)
            if spot == cls.OCCUPIED and nb_occupied >= limit:
                new_data.update({coord: cls.EMPTY})
            elif spot == cls.EMPTY and nb_occupied == 0:
                new_data.update({coord: cls.OCCUPIED})
        
        return new_data
            
    @classmethod    
    def get_seats_after_equilibrium(cls, data, limit, ignore_type=None):
        new_data = cls.update_seats(data, limit, ignore_type)
        return cls.get_seats_after_equilibrium(new_data, limit, ignore_type) if new_data != data else data
                    
    def part_1(self):
        data = copy.deepcopy(self.data)
        data = self.get_seats_after_equilibrium(data, 4)
        return len([1 for d in data.values() if d == self.OCCUPIED])
        
    def part_2(self):
        data = copy.deepcopy(self.data)
        data = self.get_seats_after_equilibrium(data, 5, self.FLOOR)
        return len([1 for d in data.values() if d == self.OCCUPIED])
