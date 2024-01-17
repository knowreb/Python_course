from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# creation of two d6 dice
die_1 = Die()
die_2 = Die()

# making a number of throws and placing the results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analysis of the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualisation of the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of occurence of values'}
my_layout = Layout(title='Result of throwing a double d6 die a thousand times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
