from collections import defaultdict
from utils.abstract import SolutionsAbstract
from typing import NamedTuple

    
class SolutionsDay13(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        data = inputs.splitlines()
        
        return {
            'timestamp': int(data[0]),
            'buses': data[1].split(','),
        }
    
    @staticmethod
    def next_bus(timestamp, bus_number):
        return bus_number - timestamp%bus_number
                    
    def part_1(self):
        timestamp = self.data['timestamp']
        timetable =  {
            self.next_bus(timestamp, int(bus)): int(bus)
            for bus in self.data['buses']
            if bus != 'x'
        }
        
        next_bus_arriving_in = min(timetable.keys())
        
        return timetable[next_bus_arriving_in] * next_bus_arriving_in 
    
    def part_2(self):
        pass
