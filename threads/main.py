import threading
import time

def get_data(data):
    while True:
        print(threading.current_thread().name," -- data : " , data)
        time.sleep(3)

th1 = threading.Thread(target=get_data, args=("UniKey=0xn21skl",), name="Thread 1")

th1.start()


i = 0
while True:
    i += 1
    print(i)
    time.sleep(1)

    if i % 10 == 0:
        print("active threads:",threading.active_count())
        print("enum:",threading.enumerate())
        print("th1 is alive:", th1.is_alive())

