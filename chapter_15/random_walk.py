from random import choice

class RandomWalk():
    """A class designed to generated random stray """
    def __init__(self, num_points=5000):
        """Initialisation of stray attributes"""
        self.num_points = num_points

        #the origin point has coordinates
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generation of all points for random wandering"""

        #To perform the steps until the expected number of points is reached
        while len(self.x_values) < self.num_points:

            """determination of the direction and the distance to be travelled in that direction"""
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #rejected moves that lead nowhere
            if x_step == 0 and y_step == 0:
                continue

            # determination of the following x and y values
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)