# Basic snowflake example

from pico_neopixel import Neopixel
from machine import Timer
import random
pixels = 275
strip = Neopixel(pixels, 0, 28, "GRB")
strip.brightness(30)


white = (255, 255, 255)

snowflakePos = 270
state = 1 # 1 is 40; 2 is 10
def move_snowflake():
    global snowflakePos, state
    strip.clear()
    strip.set_pixel(snowflakePos, white)
    strip.show()
    if state == 1:
        snowflakePos -= random.randint(39, 41)
        state = 2
    elif state == 2:
        snowflakePos -= random.randint(9, 11)
        state = 1
    if snowflakePos < 0:
        snowflakePos = 270
        state = 1 


tim = Timer()

tim.init(freq=2, mode=Timer.PERIODIC, callback=lambda t: move_snowflake())