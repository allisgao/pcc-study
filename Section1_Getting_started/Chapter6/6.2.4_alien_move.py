#! python3
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: %s.' % (str(alien_0['x_position'])))

# move aliens to right
# the lenth of moving depends on the speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this mast be very fast
    x_increment = 3

# the new position equals to it plus the addition
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: %s' % (str(alien_0['x_position'])))

