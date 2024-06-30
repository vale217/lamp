import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D2
num_pixels = 16

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

PURPLE = (180, 0, 255)
OFF = (0,0,0)

while True:
    print(switch.value)
    if (switch.value==True):
        pixels.fill(PURPLE)
        pixels.show()
        time.sleep(1)  # debounce delay
    else:
        pixels.fill(OFF)
        pixels.show()
        time.sleep(1)  # debounce delay
# Write your code here :-)
