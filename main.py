import random

import datetime,os

os.system("clear")

otp=int(random.randint(1000000000,9999999999999))

otp=list(str(otp))
otpnew=""

for i in range(6):
    otpnew.append(random.choice(otp)

time=datetime.datetime.now().hour

def greet():

    if time>=0 and time<12:

        print('Good morning!')

    elif time<=12 and time>16:

        print("Good afternoon!")

    else:

        print('Good evening!')


print(f"{great} sir ! Please don't share this OTP with anyone\nYour OTP is {otpnew}\nI repet your OTP is {otpnew}\n Good-Bye")
