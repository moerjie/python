'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-31 18:34:26
FilePath: \data_show\die_6_visual.py
'''
from Die import Die
import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
frequencies = []
max_result = die_1.num_sides + die_2.num_sides+die_3.num_sides
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()+die_3.roll()
    results.append(result)

for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
# print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.add('D6+D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
