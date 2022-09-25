from plotly.graph_objs import Scatter, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
x_values = rw.x_values
y_values = rw.y_values

data = [Scatter(x=x_values, y=y_values, mode='markers')]
x_axis_config = {'title': 'x axis'}
y_axis_config = {'title': 'y axis'}
my_layout = Layout(title='Results of a random walk', xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='rw.html')
