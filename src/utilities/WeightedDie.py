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
class WeightedDie:
    def __init__(self):
        self._partial_sums = {}
        self._face_value = 1

    def __weights_conform(self, weights: list[int]) -> bool:
         if len(weights) < 2: #False if it is a coin
             return False
         if any(weight < 0 for weight in weights):# false if weight DNE
             return False 


    def __partial_sums(self, weights: list[int]) -> dict[int, int]:
        '''
        same algo as before
        '''
        _partial_sums={}
        sum = 0
        for i, weight in enumerate(weights):
            sum += weight 
            _partial_sums [i+1] = sum
        return _partial_sums
   
    def __partial_sums_conform(self) -> bool:
        values = list(self._partial_sums.values())
        return all(values[i] <= values [i+1] for i in range (len(values)-1) and conforms_to_a_die(values ))


    def get_face_value(self) -> int:
        """
        Return the face value of the die.
        """
        return self._face_value

    def roll(self) -> int:
       r = random.randint(1, max(self._partial_sums.values()))
       for key, value in self._partial_sums.items():
            if r <= value:
                self._face_value = key 
                return key

    def set_weights(self, weights: list[int]):
        ''''
        make it a coin if bad
        '''

        if not self.__weights_conform(weights):
            self._partial_sums = self.__partial_sums([1, 1]) 
        
        self._partial_sums = self.__partial_sums(weights)
     

# def partial_sums(weights : list[int]) -> dict[int, int]:
#     """ Partial Sums algo
# 1. empty dict
# 2. init sum
# 3. iterate weight addition over the list, store in the sum
# 4. store in dict
# 5. return dict 
# """
#     partial_sums_dict = {}
#     sum = 0
#     for i, weight in enumerate(weights):
#         sum += weight
#         partial_sums_dict[i + 1] = sum
#     return partial_sums_dict

# def roll(weights : list[int]) -> int:
#      """ Roll function algo
# 1. call partial sum dict creation and set to var
# 2. randomize beweteen 1 and max value in dict
# 3. check if partial sum is greater than random sum
# 4. iterate over each item in dict 
# 5. return value from dict if random number is less than the weight 
# """
#      has_negative_values(weights)
#      ps_dict = partial_sums(weights)
#      conforms_to_a_die(list(ps_dict.values()))
#      is_monotonically_increasing(ps_dict)
#      r = random.randint(1, max(ps_dict.values()))
#      for key, value in ps_dict.items():
#         if r <= value:
#             return key


    