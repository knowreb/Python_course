alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# create an empty list for storing strangers
aliens = []

# creation of 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# displaying the total number of strangers created
print(f"Total number of aliens: {len(aliens)}")

# create an empty list for storing strangers
aliens = []
# creation of 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# displaying the first five aliens:
for alien in aliens[:5]:
    print(alien)
print('...')
