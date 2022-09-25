# Error is not there. Pyright is being irrational.
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two dice to experiment.
die_1 = Die(6)
die_2 = Die(6)

# Make some rolls, and store results in a list.
results = [(die_1.roll() * die_2.roll()) for roll_num in range(1000)]

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying two rolling D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_x_d6.html')
