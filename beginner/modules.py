import time
# Code to print 10 random numbers between 1 -> 100 (Uses random module).
import random

for i in range(10):
    print(random.randint(1, 100))
#------------------------
time.sleep(0.5)
# Code to list 5 randints, followed by pi because why not (Uses Math module)?
import math

for I in range(5):
    print(random.randint(1, 25))
print(math.pi)
#------------------------
time.sleep(0.5)
# Code to only import randint from the random module.
from random import randint

for i in range(5):
    print(randint(1, 25))
#------------------------
time.sleep(0.5)
# Code to import math and rename it to "m".
import math as m

print(m.pi)
