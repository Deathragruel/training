# There is no error here. Just pyright not detecting the modules.
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks as long as the program is active.
while True:
    rw = RandomWalk(100000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    ax.scatter(0, 0, c='white', edgecolors='none', s=10, label='starting point')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='darkblue', edgecolors='none',
               s=10, label='ending point')
    ax.legend(loc='upper left')

    # Remove the axis.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk (y/n): ")
    if keep_running == 'n':
        break
