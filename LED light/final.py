import board
import neopixel
import time

pixel_pin = board.D2   #the ring data is connected to this pin
num_pixels = 12        #number of leds pixels on the ring

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

A = (138, 218, 227)
B = (78, 203, 217)
C = (120, 180, 214)
D = (78, 166, 217)
E = (50, 101, 219)
F = (0, 57, 201)
WHITE = (250, 250, 250)
OFF = (0,0,0)

while True:
    pixels[0] = A
    pixels.show()     #required to update pixels
    time.sleep(1)

    pixels[1] = B
    pixels.show()
    time.sleep(1)

    pixels[2] = C
    pixels.show()
    time.sleep(1)

    pixels[3] = D
    pixels.show()
    time.sleep(1)

    pixels[4] = E
    pixels.show()
    time.sleep(1)

    pixels[5] = F
    pixels.show()
    time.sleep(1)

    pixels[6] = WHITE
    pixels.show()
    time.sleep(1)

    pixels[7] = WHITE
    pixels.show()
    time.sleep(1)

    pixels[8] = WHITE
    pixels.show()
    time.sleep(1)

    pixels[9] = WHITE
    pixels.show()
    time.sleep(1)

    pixels[10] = WHITE
    pixels.show()
    time.sleep(1)

    pixels[11] = WHITE
    pixels.show()
    time.sleep(1)

    pixels[12] = WHITE
    pixels.show()
    time.sleep(1)



