import random

# Creating random integers
print(random.randint(2, 23)) # inclusive

# Generates a random float between 0 and 1
print(random.random())

# Generating random float between a, b -- inclusive
print(random.uniform(1, 4))

# heads or tails

random_num = random.randint(0, 1)
if random_num == 0:
    print('Tails')
else:
    print('Heads')