import matplotlib.pyplot as plt, pygal

from random_walk import RandomWalk


# repeat
while True:

    # create a RandomWalk instance, and draw all contended points.
    rw = RandomWalk(500)
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    ## pygal
    hist = pygal.Bar()
    hist.x_labels = [ x for x in rw.x_values]
    hist.add('results', rw.y_values)
    #hist.y_labels = [ y for y in rw.y_values]
    hist.render_to_file('rw_pygal.svg')

    # keep running
    keep_running = input("Make another walk? (y/n)")
    if keep_running.lower() == 'n':
        break
