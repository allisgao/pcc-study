# coding=utf-8

from random import choice

class RandomWalk():
    """ to generate a random-walk number"""

    def __init__(self, num_points=5000):
        """ initialize random-walk's attribute"""
        self.num_points = num_points

        # all random-walk begins with (0, 0)
        self.x_values = [0]
        self.y_values = [0]


    def get_step(self):
        """ Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step


    def fill_walk(self):
        """ compute all points """

        # continueous walking, until to the pointed length
        while len(self.x_values) < self.num_points:

            # farword directions and distances
            x_step = self.get_step()
            y_step = self.get_step()

            # refuse stay in (0, 0)
            if x_step == 0 and y_step == 0:
                continue

            # compute next's x and y value
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
