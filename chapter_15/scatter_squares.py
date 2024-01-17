import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Wistia, s=10)

# definition of chart title and axis labels
ax.set_title('Squares of numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Squares of the values', fontsize=10)

# definition of label sizes
ax.axis([0, 1100, 0, 1100000])

plt.show()
