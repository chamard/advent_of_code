from collections import defaultdict
from utils.abstract import SolutionsAbstract
from typing import NamedTuple, List
import re
from collections import defaultdict
from functools import reduce


class SolutionsDay22(SolutionsAbstract):
     
    @staticmethod
    def prepare_data(inputs):
        inputs = re.sub(r"(Player [1-2]:)",'', inputs).strip().split('\n\n\n')
        player_1 , player_2 = list(map(lambda a:map(int, a.splitlines()), inputs))
        return {
            'player_1': list(player_1),
            'player_2': list(player_2),
        }

    @staticmethod
    def play(player_1, player_2):
        card_1, card_2 = player_1.pop(0), player_2.pop(0)
        winner = player_1 if card_1 > card_2 else player_2
        winner.extend([max(card_1, card_2), min(card_1, card_2)])
        return player_1, player_2
    
    @classmethod
    def get_round_winner(cls, player_1, player_2):
        card_1, card_2 = player_1[0], player_2[0]
        if card_1 < len(player_1) and card_2 < len(player_2): # new game
            aaa ,_ = cls.get_game_winner(player_1[1:card_1+1], player_2[1:card_2+1])
            return aaa
        elif card_1 > card_2:
            return 1
        else:
            return 2

    @classmethod
    def get_game_winner(cls, player_1, player_2):
        round_winner, winner = 1 , None
        previous = set()
        while (len(player_1) > 0  and len(player_2)>0):
            if tuple(player_1) in previous:
                return 1, None
            round_winner = cls.get_round_winner(player_1, player_2)
            card_1, card_2 = player_1.pop(0), player_2.pop(0)
            winner = player_1 if round_winner==1 else player_2
            winner.extend( {1: [card_1, card_2], 2:[card_2, card_1]}[round_winner])
        return round_winner, winner

    @staticmethod
    def get_score(winner):
        return sum([(i+1)*v for i, v in enumerate(winner[::-1])])

    def part_1(self):
        player_1, player_2 = self.data['player_1'].copy(), self.data['player_2'].copy()

        while len(player_1) > 0  and len(player_2)>0:
            player_1, player_2 = self.play(player_1, player_2)

        winner = player_1 if len(player_1)>0 else player_2
        return self.get_score(winner)

    def part_2(self):
        player_1, player_2 = self.data['player_1'].copy(), self.data['player_2'].copy()
        _, winner = self.get_game_winner(player_1, player_2)
        return self.get_score(winner)
