import csv
import matplotlib.pyplot as plt

with open('darts.csv', newline = '') as csvfile:
    csv_reader = csv.reader(csvfile)
    list = [[float(element) for element in row] for row in csv_reader]

x_coords = [list[i][0] for i in range(len(list))]

y_coords = [list[i][1] for i in range(len(list))]

fig, ax = plt.subplots()

ax.scatter(x_coords, y_coords, color = 'black', marker = '+')

ax.set_title('Dart Hits', pad = 15)
ax.set_xlabel('x', loc='right')
ax.set_ylabel('y', loc='top', rotation = 'horizontal')
ax.axis([-4, 4, -4, 4])
ax.tick_params(colors = 'blue')
ax.xaxis.label.set_color('blue')
ax.yaxis.label.set_color('blue')
ax.spines['left'].set_color('blue')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_color('blue')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.show()