alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien turned {alien_0['color']}!")

new_points = alien_0['points']

print(f"You just earned {new_points} points!")
del alien_0['points']
print(alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_0['speed'] = 'medium'
print(alien_0)
print(f"Original position: {alien_0['x-position']}")
# Move the alien to the right
# Determine how far to move the alien based on it's current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
elif alien_0['speed'] == 'fast':
	x_increment = 3
# The new position is the old position plus the increment
alien_0['x-position'] = alien_0['x-position'] + x_increment
print(f"New position: {alien_0['x-position']}")