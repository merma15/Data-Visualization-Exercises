import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks, as long as the program is active.
while True:
    #make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()
    #plot in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)#alter the size to fill the screen
    point_numbers = list(range(rw.num_points))
    ax.plot(rw.x_values, rw.y_values, linewidth=5)
    
    #Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors='none', s=100)

    #Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break