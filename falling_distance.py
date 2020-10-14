# Falling distance = 1/2 * gt^2

# Gravitional acceleration
GRAVITATIONAL_ACCELERATION  = 9.8

def falling_distance(time):
    distance = (1/2) * GRAVITATIONAL_ACCELERATION * time **2
    return distance

print('Number of seconds: ', '\t Falling distance:')
print('- - - - - - - - - - - - - - - - - - - - -')

for seconds in range(1, 10 + 1):
    distance_of_falling = falling_distance(seconds)
    print('{} second '.format(seconds), '\tYou fell {:.1f} meters'.format(distance_of_falling),
    sep='\t')
