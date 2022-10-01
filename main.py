import random

import datetime,os

otp = int(random.randint(1000000,999999999))

time=datetime.datetime.now().hour

def greet():
    # greet to user
    if time>=0 and time<12:
        print('Good morning!')

    elif time<=12 and time>16:
        print("Good afternoon!")

    else:
        print('Good evening!')


print(f"{great} sir ! Please don't share this OTP with anyone\nYour OTP is {otp}\nI repet your OTP is {otp}\n Good-Bye")
