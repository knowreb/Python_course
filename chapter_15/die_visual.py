from die import Die

# creation of the D6
die = Die()

#to perform a number of tosses and put the results on a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

# analysis of the results
from die import Die

# creation of the D6
die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analysis of the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# creation of histogram

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die
# analysis of the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualisation of the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of occurence of values'}
my_layout = Layout(title='Result of throwing a single d6 die a thousand times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
