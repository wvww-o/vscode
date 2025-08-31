from die import Die
import pygal
die=Die()
results=[]

for roll_num in  range(1000):
    result=die.roll()
    results.append(result)

frequencies=[]

for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist=pygal.Bar()
hist.title="Resluts of rolling one D6 1000 times"
hist.x_lables=['1','2','3','4','5','6']
hist.y_title="frequency"
hist.x_title="results"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
