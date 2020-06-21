import random

# by using seed, we will get the same random numbers
random.seed(0)
for _ in range(10):
    print(random.randint(10, 20), random.random())
