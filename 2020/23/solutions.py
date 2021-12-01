from collections import defaultdict
from utils.abstract import SolutionsAbstract
from typing import NamedTuple, List
import re
from collections import defaultdict
from functools import reduce

class Node:
    def __init__(self, data, other=None):
        self.data = data
        self.next = other
    
    def get_3_next(self):
        return [self.next, self.next.next, self.next.next.next]

class LinkedList:
    def __init__(self, nodes=None):
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
        node.next = self.head 
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node.data not in nodes:
            nodes.append(node.data)
            node = node.next
        return " -> ".join(map(str, nodes))
    
    def play(self):
        current_value = self.head.data
        pick_ups_values  = [el.data for el in self.head.get_3_next()]
        for 

class SolutionsDay23(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        return  LinkedList([int(el) for el in inputs.strip()])

    def part_1(self):
        current = self.data[0]
        pick_up= self.data[1:4]
        remaining = self.data[4:]

        distination = min([el for el in remaining if el < current])
        import pdb;pdb.set_trace()

        pass

    def part_2(self):
        pass
