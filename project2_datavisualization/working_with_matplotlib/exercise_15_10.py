from random import choice

class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        numbers = range(1, self.num_sides+1)
        number_rolled = choice(numbers)
        return number_rolled
