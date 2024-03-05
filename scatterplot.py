import csv
import matplotlib.pyplot as plt

with open('darts.csv', newline = '') as csvfile:
    csv_reader = csv.reader(csvfile)
    list = [[float(element) for element in row] for row in csv_reader]
    # for row in csv_reader:
    #     inner_list = []
    #     for element in row:
    #         inner_list.append(float(element))
    #     list.append(inner_list) 
    print(list)

x_coords = []
for i in range(len(list)):
    x_coords.append(list[i][0])
print(x_coords)

y_coords = []
for i in range(len(list)):
    y_coords.append(list[i][1])
print(y_coords)

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

ax.yaxis.label.set_color('blue')

plt.show()