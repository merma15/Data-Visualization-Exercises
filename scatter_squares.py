import matplotlib.pyplot as plt

#data calculations automatically
x_values = range(1, 1001)
y_values = [i**2 for i in x_values] 

plt.style.use('seaborn')
fib, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#ax.scatter(x_values, y_values, c='grey', s=10) c stands for 'color' and s for 'size of the point
#ax.scatter(x_values, y_values, c=(0.0, 0.6, 0.0), s=10)  for RBG we use values from 0 to 1 not from 0 up to 255
#Values closer to 0 produces dark colors, and values closer to 1 produce lighter colors
#set the chart title and lable axes


ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.savefig('sqaures_plot.png', bbox_inches='tight')