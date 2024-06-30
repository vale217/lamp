import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255,255,255)
OFF = (0,0,0)

colors = [RED,YELLOW,GREEN,CYAN,BLUE,PURPLE,WHITE]
now=0

while True:
    print(switch.value)
    if (switch.value==False):    #detect the button press
        now=now+1
        if (now >= 7): #7 colors in the list
            now=0
        pixels.fill(colors[now])
        pixels.show()
    time.sleep(0.12)  # debounce delay
