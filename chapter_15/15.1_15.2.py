import matplotlib.pyplot as plt

x_values = range(5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.twilight_shifted, s=5)

ax.set_title('Cube of numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Cube of the values', fontsize=10)

ax.tick_params(axis='both', which='major', labelsize='10')
ax.axis([0, 5100, 0, 130_000_000_000])

plt.show()