import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# definition of chart title and axis labels
ax.set_title("Squares of numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Squares of the values", fontsize=10)

# definition of label sizes
ax.tick_params(axis='both', labelsize=10)

plt.show()