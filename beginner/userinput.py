import time
# Code to input username and prints out:
print("Hello. Enter your Username:")
username=input()
print("Hello,", username, "Have fun.")
time.sleep(0.5)
# Basic if statement lol:
print ("Hello. Enter your Age:")
age=input()
if age>="12":
    print("Welcome, You are above the age requirement.")
else:
    print("Oh Well, don't tell my boss I let you in.")
time.sleep(0.5)
# Code to calculate two variables: rate / distance:
print("Input a rate (e.g. 10) and distance (e.g. 120):")
rate = float(input("Rate: "))
distance = float(input("Distance: "))
print("Time:", (distance / rate))
