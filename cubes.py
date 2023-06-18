import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [i**3 for i in x_values] #output we want to see theri graphs

#variable declarations
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.pink, s=9)

#chart and axes styling
ax.set_title('Cubes Numbers', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('cubes of Numbers', fontsize=14)

#set the size of labels
ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 5100, 0, 125100000000])

plt.savefig('cubes_plot.png',bbox_inches='tight')
