# To Generate Single Random Numbers

import random

'''n = random.random()

print (n)'''

# To Generate Numbers in Range

'''n = random.randint(1,26)

print(n)'''


# To Generate List of Random Numbers in Range Using for loop

'''randomlist = []

for i in range(0,5):
    n = random.randint(1,69)
    randomlist.append(n)
print (randomlist)'''

# To Generate list of numbers in range using sample()

randomlist = random.sample(range(1,69),5)

print(randomlist)
