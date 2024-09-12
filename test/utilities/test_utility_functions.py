import unittest
import random
from src.utilities.utility_functions import *
from src.utilities.weighted_die_roller import *
class TestUtilityFunctions(unittest.TestCase):

    def test_has_negative_values(self):
        self.assertTrue(has_negative_values([-1, 2, 3]))  
        self.assertTrue(has_negative_values([-5, 2, 3]))  
        self.assertFalse(has_negative_values([0, 1, 2]))  
        self.assertFalse(has_negative_values([1, 2, 3]))  

    def test_conforms_to_a_die(self):
        self.assertTrue(conforms_to_a_die([1, 2, 3]))  
        self.assertFalse(conforms_to_a_die([1, 2, 2])) 
        self.assertFalse(conforms_to_a_die([3, 3, 3]))  
        self.assertFalse(conforms_to_a_die([5, 3, 0,1]))
        self.assertTrue(conforms_to_a_die([1, 2, 3, 4])) 
        self.assertFalse(conforms_to_a_die([0, 1, 2]))  
        self.assertTrue(conforms_to_a_die([])) 

    def test_is_monotonically_increasing(self):
        self.assertTrue(is_monotonically_increasing({1: 3, 2: 5, 3: 6, 4: 12, 5: 16, 6: 17})) 
        self.assertFalse(is_monotonically_increasing({1: 3, 2: 3, 3: 2, 4: 5, 5: 11, 6: 12}))  
        self.assertFalse(is_monotonically_increasing({1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5}))  
        self.assertTrue(is_monotonically_increasing({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}))  
        self.assertTrue(is_monotonically_increasing({}))    


