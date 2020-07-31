# Jaxon Terrell
# 7/24/20
# Game that asks player to wait a specific amount of time before they press anything,
# player wants to guess as close to specified time as they can
import random
import time


def waiting_game():
    time_used = 0
    wait_for = random.randint(1,10)
    start_game = input(f"Your target time is  {wait_for} seconds.\n---Press Enter to Begin---")
    if start_game == "":
        start_time = time.time()
        end_game = input(f"\n...Press Enter again after {wait_for} seconds...")
        if end_game == "":
            end_time = time.time()
            time_used = end_time - start_time
            print(f"\nElapsed time: {time_used} seconds")
            if time_used < wait_for:
                difference = wait_for - time_used
                print(f"({difference} seconds too fast)")
            elif time_used > wait_for:
                difference = time_used - wait_for
                print(f"({difference} seconds too slow)")
            else:
                print("Congratulations! You have inhuman reaction time and somehow nailed it right on the dot!")


if __name__ == "__main__":
    waiting_game()

