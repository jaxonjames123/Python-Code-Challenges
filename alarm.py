# Jaxon Terrell
# 7/31/20
# Plays a sound and prints a message at a set time

from playsound import playsound
import time


def alarm(alarm_time, sound, message):
    if time.time() == alarm_time:
        playsound(sound)
        print(message)