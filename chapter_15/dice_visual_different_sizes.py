from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#creation of d6 and d10 dice
die_1 = Die()
die_2 = Die(10)

#Making a number of throwa to put the results on a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analysis of results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualisation of results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of occurence of values'}
my_layout = Layout(title='Result of throwing the d6 and d10 dice fifty thousand times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

