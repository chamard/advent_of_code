from collections import defaultdict
from utils.abstract import SolutionsAbstract
from typing import NamedTuple
import copy
from math import cos, sin, radians
import math
from dataclasses import dataclass

@dataclass
class Vector:
    x: int
    y: int
    
    def rotate(self, angle: int) -> None:
        angle  = radians(angle)
        qx = math.cos(angle) * self.x + math.sin(angle) * self.y
        qy = math.cos(angle) * self.y - math.sin(angle) * self.x
        self.x, self.y = qx,  qy
    
    def add(self, other: object) -> None:
        self.x += other.x
        self.y += other.y
    
    def multiply(self, factor):
        return self.__class__(self.x * factor, self.y * factor)


DIRECTIONS = {
    'N': lambda val: Vector(0, val),
    'S': lambda val: Vector(0, -val),
    'E': lambda val: Vector(val, 0),
    'W': lambda val: Vector(-val, 0),
}

class Ship:
    
    def __init__(self, waypoint: Vector):
        self.position = Vector(0,0)
        self.waypoint = waypoint
    
    def move_ship(self, update_element, instruction, value):
        if instruction == 'F':
            self.position.add(self.waypoint.multiply(value))
        elif instruction in ('N', 'S', 'E', 'W'):
            direction = DIRECTIONS[instruction](value)
            # in part 1 we update the position of the boat
            # in part 2 we update the waypoint vector
            getattr(self, update_element).add(direction) 
        elif instruction in ('R', 'L') :
            value = {'R': lambda x: x, 'L': lambda x: -x}.get(instruction)(value)
            self.waypoint.rotate(value)

    def get_manathan_distance(self):
        return abs(self.position.x) + abs(self.position.y)

    
class SolutionsDay12(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        return [(line[0], int(line[1::]))for line in inputs.splitlines()]
                        
    def part_1(self):
        waypoint = Vector(1, 0)
        ship = Ship(waypoint)
        for arg in self.data:
            ship.move_ship('position', *arg)
            print(ship.waypoint)
        return ship.get_manathan_distance()
        
    def part_2(self):
        waypoint = Vector(10, 1)
        ship = Ship(waypoint)
        for arg in self.data:
            ship.move_ship('waypoint', *arg)
        return ship.get_manathan_distance()
