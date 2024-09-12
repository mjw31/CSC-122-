import random

class Die():
    """A simple, 6-sided die class"""

    def __init__(self):
        self._num_sides = 6
        self._face_value = 0
        self.roll()

    def roll(self) -> int:
        self._face_value = random.randint(1, self._num_sides)
        return self._face_value

    # accessor method; overkill in Python,
    # but is good practice for the future: Java
    def get_face_value(self) -> int:
        return self._face_value
# Populate and print a dictionary of die 
    # rolls to assess fairness
    results = dict()
    for _ in range(600):
        if die.roll() not in results:     
            results[die.get_face_value()] = 1   
        else:
            results[die.get_face_value()] += 1

    print(results)

