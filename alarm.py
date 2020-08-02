# Jaxon Terrell
# 7/31/20
# Allows user to set an alarm that plays a sound and prints a message at set time

from playsound import playsound
import sched
import time


def set_alarm(alarm_time, sound_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, playsound, argument=(sound_file,))
    print("Alarm has been set for ", time.asctime(time.localtime(alarm_time)))
    s.run()