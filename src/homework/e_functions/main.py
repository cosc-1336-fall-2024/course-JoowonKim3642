#main

from value_return import get_hour, get_minutes, get_seconds
import time

def main():

    epoch_seconds = 3800

    hour = get_hour(epoch_seconds)
    minute = get_minutes(epoch_seconds)
    seconds = get_seconds(epoch_seconds)
    
    print(f"The time is {hour:02}:{minute:02}:{seconds:02}")

    print(time.strftime('%Y.%m.%d - %H:%M:%S'),"UTC")

main()