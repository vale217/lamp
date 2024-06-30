import time
import board
import neopixel

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

while True:
    for num in range(0,254,2):   #fade in loop
        COLOR=(num,0,0)
        for light in range (0,16,1):
            pixels[light]=COLOR
        pixels.show()
    for num in range(254,0,-2):   #fade out loop
        COLOR=(num,0,0)
        for light in range (0,16,1):
            pixels[light]=COLOR
        pixels.show()
