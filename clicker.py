from time import sleep
from pynput.keyboard import Key, Listener
from pyautogui import click
from threading import Thread

print("Program başladı...")

class ClickBoard(Thread):
    def __init__(self):
        super(ClickBoard, self).__init__()
        self.running = False
        
    def star_stop(self):
        self.running = not self.running
        
    def run(self):
        while True:
            while self.running:
                sleep(0.5)
                click()
                
clicker = ClickBoard()
clicker.start()

def on_press(key):
    if key == Key.f4:
        clicker.star_stop()
        
with Listener(on_press=on_press) as listen:
    listen.join()
