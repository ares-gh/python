import time
import math
# Code to count how many letters are in your surname, len().
surname = input("Enter your surname: ")
count = len(surname)
print ("Your surname has", count, "letters in it. ")
# Code to input a number, finds the square root of it.
sqrnum = input("Enter any number: ")
print ("The square root of", ( int(sqrnum), "is", math.sqrt( int(sqrnum) )))
time.sleep(0.5)
# Code to use the "Hello" func from "hello.py" to say hello to ares.
from hello import hello
hello("ares")
