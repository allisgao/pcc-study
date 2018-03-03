import matplotlib.pyplot as plt

from random_walk import RandomWalk

# repeat
while True:

    # create a RandomWalk instance, and draw all contended points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # set draw-window size
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

    # emphase start and stop point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # hide axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # keep running
    keep_running = input("Make another walk? (y/n)")
    if keep_running.lower() == 'n':
        break
