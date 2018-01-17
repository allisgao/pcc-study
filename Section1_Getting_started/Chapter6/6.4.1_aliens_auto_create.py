#! python3

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: %s" %(str(len(aliens))))
#print(aliens)
print('...\n')
# 将前3个外星人修改为：颜色-yellow, speed-medium， points-5
for alien in aliens[:3]:
    if alien['color'] != 'yellow':
        alien['color'] = 'yellow'
        if alien['points'] != 10:
            alien['points'] = 10
            if alien['speed'] != 'medium':
                alien['speed'] = 'medium'
print(aliens[:5])









