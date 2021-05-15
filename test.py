import time
import json
from threading import Thread

start_time = time.perf_counter()

def subscribe(id, period):
    subscribers_file = open("dictionaries/subscribers.json", 'r', encoding="utf-8")
    subscribers_dict = json.load(subscribers_file)
    subscribers_dict[id] = period
    subscribers_file.close()
    subscribers_file = open("dictionaries/subscribers.json", 'w', encoding="utf-8")
    json.dump(subscribers_dict, subscribers_file, indent=4, ensure_ascii=False)
    subscribers_file.close()

def knock():
    print(f"Knock-knock!")

def timer(func, minutes=1):
    while True:
        time.sleep(minutes*30)
        func()

th_timer = Thread(target=timer, args=(knock, 1))
th_timer.start()
while True:
    a, b = input().split()
    subscribe(a, b)