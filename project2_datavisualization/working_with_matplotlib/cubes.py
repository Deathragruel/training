import matplotlib.pyplot as plt

input_values = range(1, 5001)
cubes = [x**3 for x in input_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.cool, s=10)

ax.set_title('Cube number graph', fontsize=14)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of value', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 5100, 0, 130000000000])
plt.show()
