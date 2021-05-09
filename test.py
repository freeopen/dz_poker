'''
Author: freeopen
Date: 2021-05-09 18:01:52
LastEditTime: 2021-05-09 19:12:33
Description: file content
FilePath: /holdem_calc/test.py
'''
from poker import Range 
from poker.hand import Combo 

import holdem_calc 
import holdem_functions 

import numpy as np 

hero_odds = [] 
hero_range_odds = []


hero_hand = Combo('KsJc') 
print(hero_hand)

flop = ["Qc", "Th", "9s"] # the flop 
board = flop # the board equals the flop 
villan_hand = None # no prior knowledge about the villan 
exact_calculation = True #  calculates exactly by simulating the set of all possible hands 
verbose = True # returns odds of making a certain poker hand, e.g., quads, set, straight 
num_sims = 1 # ignored by exact_calculation = True 
read_from_file = None # we are not reading hands from file


villan_range = Range('99+, AT+, KJ+')
print("#combo combinations:" + str(len(villan_range.combos)))

# odds = holdem_calc.calculate_odds_villan(board, exact_calculation,  
#                             num_sims, read_from_file ,  
#                             hero_hand, villan_hand,  
#                             verbose, print_elapsed_time = True)

# print(odds[0])

items = [holdem_calc.calculate_odds_villan(board, exact_calculation,  
                            num_sims, read_from_file ,  
                            hero_hand, villan_hand,  
                            verbose, print_elapsed_time = False) for villan_hand in villan_range.combos] 

odds = {} 
[odds.update({odd_type: np.mean([res[0][odd_type] for res in items if res])}) for odd_type in ["tie", "win", "lose"]]
print(odds)

for hand_ranking in holdem_functions.hand_rankings: 
    print(hand_ranking +": " + str(np.mean([res[1][1][hand_ranking] for res in items if res])))