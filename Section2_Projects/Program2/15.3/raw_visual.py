import matplotlib.pyplot as plt

from random_walk import RandomWalk

# repeat
while True:

    # create a RandomWalk instance, and draw all contended points.
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    # keep running
    keep_running = input("Make another walk? (y/n)")
    if keep_running.lower() == 'n':
        break
