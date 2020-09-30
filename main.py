import random

import datetime,os



os.system("clear")



otp=int(random.randint(100000,999999))

	

time=datetime.datetime.now().hour



def greet():

    if time>=0 and time<12:

        print('Good morning!')

    elif time<=12 and time>16:

        print("Good afternoon!")

    else:

        print('Good evening!')



greet()





print(f"Please don't share this OTP with anyone\nYour OTP is {otp}\nI repet your OTP is {otp}\nGood-Bye")
