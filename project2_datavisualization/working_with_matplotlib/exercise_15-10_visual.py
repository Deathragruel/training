# False warning by pyright.
import matplotlib.pyplot as plt
from exercise_15_10 import Die

die = Die()

results = [die.roll() for x in range(1000)]
num_sides = die.num_sides
frequencies = [results.count(value) for value in range(1, num_sides+1)]
x_values = [x for x in range(1, num_sides+1)]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

ax.bar(x_values, frequencies)
ax.plot()
ax.set_title('Results of a 1000 D6 die rolls')
ax.set_xlabel('Roll values')
ax.set_ylabel('Amount of times the value was rolled.')

plt.show()
