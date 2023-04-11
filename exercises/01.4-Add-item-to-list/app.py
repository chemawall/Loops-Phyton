#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
extra10 = random.randint(1, 10)

def loop():
    for i in range(10):
        my_list.append(extra10)
    print(my_list)   

loop()
