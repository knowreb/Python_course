from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#creation of d6 and d6 dice
die_1 = Die(6)
die_2 = Die(6)

#Making a number of throwa to put the results on a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

#Analysis of results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#Visualisation of results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of occurence of values'}
my_layout = Layout(title='Result of throwing twice the d6 dice thousand times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='15.9.html')