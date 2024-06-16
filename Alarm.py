from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapsed = 00
    print(CLEAR)
    while(time_elapsed < seconds):
        time.sleep(1) # wait for 1 sec
        time_elapsed+=1

        time_left = seconds - time_elapsed

        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")

    playsound('/Users/vishwavinayak/Documents/Programming/Projects/Alarm/Alarm.mp3')

minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter Seconds: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
