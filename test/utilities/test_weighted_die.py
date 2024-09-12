import unittest
from src.utilities.WeightedDie import WeightedDie
import random

class TestWeightedDieRoller(unittest.TestCase):
    """
    Same borderline test values as used last time(increasing decreasing etc)
    """

    def run_die_rolls(self, die: WeightedDie, weights: list[int], expected_probs: list[float]):
        results = [0] * (len(weights) + 1)
        NUM_ROLLS = 1000000
        for _ in range(NUM_ROLLS):
            results[die.roll()] += 1

        del results[0] 

        for expected, computed in zip(expected_probs, results):
            self.assertAlmostEqual(expected, computed / NUM_ROLLS, places=2)  # Very loose bounds

    def compute_probs_then_run_rolls(self, weights: list[int]):
        # Compute expected probabilities
        s = sum(weights)
        expected = [w / s for w in weights]

        # run the test
        die = WeightedDie() #init class WeightedDie into variable
        die.set_weights(weights)
        self.run_die_rolls(die, weights, expected)

    def test_partial_sums(self):
        die = WeightedDie()
        self.assertEqual(die._WeightedDie__partial_sums([3, 2, 1, 6, 4, 1]), {1: 3, 2: 5, 3: 6, 4: 12, 5: 16, 6: 17})
        self.assertEqual(die._WeightedDie__partial_sums([1, 1, 1, 1]), {1: 1, 2: 2, 3: 3, 4: 4})
        self.assertEqual(die._WeightedDie__partial_sums([0, 0, 0, 0]), {1: 0, 2: 0, 3: 0, 4: 0})
        self.assertEqual(die._WeightedDie__partial_sums([]), {})

    def test_roll(self):
        # Fair 6-sided die test
        self.compute_probs_then_run_rolls([1, 1, 1, 1, 1, 1])

        # 7-sided die test
        self.compute_probs_then_run_rolls([1, 0, 2, 4, 1, 1, 2])

        #  TODO: Additional tests
        self.compute_probs_then_run_rolls([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.compute_probs_then_run_rolls([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.compute_probs_then_run_rolls([1]*35)  # 35 sides
