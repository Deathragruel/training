# Error is not there. Pyright is being irrational.
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two dice to experiment.
die_1 = Die(1024)
die_2 = Die(1024)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 100}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D1024 dice 10000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d1024_d1024.html')
