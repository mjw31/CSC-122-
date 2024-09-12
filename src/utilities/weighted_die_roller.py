from src.utilities.utility_functions import *
import random
import math
"""
* Simulates weighted Dice Roll with n sides
*
* Bugs:
*
* @author <Michael Wolfe>
* @date <9/4/2024>
"""
     

def partial_sums(weights : list[int]) -> dict[int, int]:
    """ Partial Sums algo
1. empty dict
2. init sum
3. iterate weight addition over the list, store in the sum
4. store in dict
5. return dict 
"""
    partial_sums_dict = {}
    sum = 0
    for i, weight in enumerate(weights):
        sum += weight
        partial_sums_dict[i + 1] = sum
    return partial_sums_dict

def roll(weights : list[int]) -> int:
     """ Roll function algo
1. call partial sum dict creation and set to var
2. randomize beweteen 1 and max value in dict
3. check if partial sum is greater than random sum
4. iterate over each item in dict 
5. return value from dict if random number is less than the weight 
"""
     has_negative_values(weights)
     ps_dict = partial_sums(weights)
     conforms_to_a_die(list(ps_dict.values()))
     is_monotonically_increasing(ps_dict)
     r = random.randint(1, max(ps_dict.values()))
     for key, value in ps_dict.items():
        if r <= value:
            return key


    