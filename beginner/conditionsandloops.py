import time
# Code to check if the statement is true or false.
word=input("Please enter a five-letter word: ")
word_length=len(word)
if word_length == 5:
    print(word, "is a five-letter word. Well done.")
elif word_length == 4:
    print(word, "is a four-letter word.")
else:
    print  (word, "is not a five-letter word.")
time.sleep(0.5)
# Code to count from 1 -> 10 (while statement).
x = 1
while x < 10:
    print (x)
    x = x + 1
time.sleep(0.5)
# Code to print a list out.
gpus=["RTX 3050", "RX 6600XT", "UHD 630", "Vega 11"]
for word in gpus:
    print (word)
time.sleep(0.5)
# Code to loop within the range of 1 -> 10.
for x in range (1, 10):
    print (x)
