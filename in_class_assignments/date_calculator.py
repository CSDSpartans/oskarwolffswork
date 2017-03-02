'''
write a function that does a countdown until christmas
'''


from datetime import datetime, timedelta
import time

christmas = datetime(2016, 12, 25)
gunnar_birthday = datetime(2016, 12, 14)
rogue_1 = datetime(2016, 12, 15, 19)

current_time = datetime.today()


def countdown_to(event):
    while datetime.today() < event:
        difference = event - datetime.today()
        print(difference)

        time.sleep(1)


countdown_to(rogue_1)
