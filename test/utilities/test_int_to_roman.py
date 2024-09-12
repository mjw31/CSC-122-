import unittest

from src.utilities.int_to_roman import to_roman

class TestIntToRoman(unittest.TestCase):

    def execute_to_roman(self, n : int, expected : str) -> None:

        computed = to_roman(n)
        self.assertEqual(computed, expected, msg = f"Found {n} -> {computed}; Expected {n} -> {expected}")

    def test_to_roman(self):
        self.execute_to_roman(-1, "")
        self.execute_to_roman(0, "")
        self.execute_to_roman(6000, "")
        self.execute_to_roman(6001, "")
        self.execute_to_roman(1, "I")
        self.execute_to_roman(2, "II")
        self.execute_to_roman(3, "III")
        self.execute_to_roman(4, "IV")
        self.execute_to_roman(5, "V")
        self.execute_to_roman(6, "VI")
        self.execute_to_roman(7, "VII")
        self.execute_to_roman(8, "VIII")
        self.execute_to_roman(9, "IX")
        self.execute_to_roman(10, "X")
        self.execute_to_roman(4444, "MMMMCDXLIV")
        self.execute_to_roman(4378, "MMMMCCCLXXVIII")
        self.execute_to_roman(2246, "MMCCXLVI")
        self.execute_to_roman(976, "CMLXXVI")
        self.execute_to_roman(5211, "MMMMMCCXI")
        self.execute_to_roman(5999, "MMMMMCMXCIX")

        

        print("Tests completed successffully.")
