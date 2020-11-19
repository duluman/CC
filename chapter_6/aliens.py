alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

new_aliens = []

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    new_aliens.append(new_alien)

print(f"Total number of aliens: {len(new_aliens)}")

for alien in new_aliens[:5]:
    print(alien)

print(new_aliens)

for alien in new_aliens[:3]:
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

for alien in new_aliens:
    print(alien)

for alien in new_aliens[3:11]:
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = 15

for alien in new_aliens:
    print(alien)

