from Die import Die
import pygal

die = Die()

results = []
frequencies = []

for roll_num in range(100000):
    result = die.roll()
    results.append(result)

for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#print(frequencies)
hist=pygal.Bar()

hist.title="Results of rolling one D6 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')