import pyautogui
import time

lyrics = open('lyrics.txt', 'r')

time.sleep(10)

for line in lyrics:
    pyautogui.typewrite(line)
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(2) 
