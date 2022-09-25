import matplotlib.pyplot as plt
import math

# This program is, for now, a failure.
input_values = [x for x in range(-360, 360)]
y_axis = []
for x in input_values:
    y = math.tan(math.radians(x))
    y_axis.append(y)
y_axis_2 = [-x for x in y_axis]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
# This divides your graph into four quadrants.
ax.axhspan(0, 0, linewidth=1, color='#808080')
ax.axvline(0, linewidth=1, color='#808080')
# Set input values to override default assumption that values start at 0.
ax.plot(input_values, y_axis, linewidth=3)
# Set chart title and label axes.
ax.set_title("Tangent Graph", fontsize=14)
ax.set_xlabel("Angle", fontsize=14)
ax.set_ylabel("Y-Axis", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Second y-axis.
ax2 = ax.twinx()
ax2.plot(input_values, y_axis_2, linewidth=3)

plt.show()
