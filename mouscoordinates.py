#! python3
import pyautogui, sys
import time
print('Press Ctrl-C to quit.')
try:
    while True:
        time.sleep(.5)
        x, y = pyautogui.position()
        print(x, y)
except KeyboardInterrupt:
    print('\n')