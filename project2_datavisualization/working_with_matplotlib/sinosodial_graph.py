import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

input_values = np.array([-360, -270, -180, -90, -60, -45, -30, 0,
30, 45, 60, 90, 180, 270, 360])
y_axis = np.array([0, 1, 0, -1, -0.87, -0.71, -0.5, 0, 0.5, 0.71, 0.87, 1, 0,
-1, 0])
xnew = np.linspace(input_values.min(), input_values.max(), 300)
spl = make_interp_spline(input_values, y_axis, k=3)  # type: BSpline
power_smooth = spl(xnew)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
# This divides your graph into four quadrants.
ax.axhspan(0, 0, linewidth=1, color='#808080')
ax.axvline(0, linewidth=1, color='#808080')

# Set input values to override default assumption that values start at 0.
ax.plot(xnew, power_smooth, linewidth=3)

# Set chart title and label axes.
ax.set_title("Sinosodial Graph", fontsize=24)
ax.set_xlabel("Angle", fontsize=14)
ax.set_ylabel("Y-Axis", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
