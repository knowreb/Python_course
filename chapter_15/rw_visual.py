import matplotlib.pyplot as plt

from random_walk import RandomWalk

#creation of a new random stray as long as the programme remains active
while True:
    #preparation of random stray data and display of points
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #display of stray data and display of points
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    #Emphasis on the first and last point of random error
    ax.scatter(0, 0, c='green', edgecolors = 'none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Hiding the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Create another random blunder? (y/n): ")
    if keep_running == 'n':
        break