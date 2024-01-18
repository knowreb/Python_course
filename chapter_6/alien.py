alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {'color': 'green'}
print(f"The alien has a colour {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien has a colour {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Initial value x-position: {alien_0['x_position']}")

# Moving a stranger to the right.
# Determining the distance to be covered by a stranger moving at a given speed.
if alien_0['speed'] == 'slow:
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #It must be a fast stranger.
    x_increment = 3

# the new position is the sum of the previous position and the x_increment value
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New value x-position: {alien_0['x_position']}")
