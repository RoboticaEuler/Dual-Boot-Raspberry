import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# 3 = GND
# 19 = 14
# 20 = 15

class Button:
    all = []
    def __init__(self, pin = board.GP14):
        self.val = False
        self.old_val = False
        self.pressed = False 
        self.self = digitalio.DigitalInOut(pin)
        self.self.direction = digitalio.Direction.INPUT
        self.self.pull = digitalio.Pull.UP
        Button.all.append(self)
    @classmethod
    def type(cls, string:str):
        for x in string:
            exec(f"temp = Keycode.{x.upper()}")
            keyboard.press(temp)
            keyboard.release(temp)
    @classmethod
    def update(cls):
        for x in cls.all:
            x.old_val = x.val
            x.val = bool(x.self.value)
            if (not x.old_val) and (x.val):
                x.pressed = True 
            else:
                x.pressed = False 

button1 = Button(board.GP14)
button2 = Button(board.GP15)
keyboard = Keyboard(usb_hid.devices)

while True:
    Button.update()
    if button1.pressed:
        with open("log.txt", "w") as f:
            f.write("0")
    if button2.pressed:
        with open("log.txt", "w") as f:
            f.write("1")