from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create a D6.
die_1 = Die(8)
die_2 = Die(8)
#die_3 = Die(8)


#make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll() #+ die_3.roll()
    results.append(result)
#print(results)
#analyse the results.

frequencies = []
max_result = die_1.num_sides * die_2.num_sides #+ die_3.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    #frequencies[value] = frequency , here we can use dictionaries
#print(frequencies)

#visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling Two D8 1000 times', 
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')