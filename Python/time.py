print("Bhavya Madan\n0901AM221026")
import time

def countdown(seconds):
    while seconds > 0:
        print("Countdown:", seconds)
        time.sleep(1)
        seconds -= 1
    print("Countdown Complete!")

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print("Timer:", remaining_time)
        time.sleep(1)
    print("Timer Complete!")

countdown(5)
timer(10)  