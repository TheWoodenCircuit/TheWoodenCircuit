from pico_neopixel import Neopixel
from machine import Timer
import time

pixels = 280
strip = Neopixel(pixels, 0, 28, "GRB")
strip.brightness(30)


# This can be replaced with other gradients or colors
gradient = [(255, 15, 123), (248, 155, 41)]


begin = 0
end = 5


def contract():
    global begin
    begin += 1
    time.sleep(0.1)
    strip.clear()
    strip.set_pixel_line_gradient(begin, end, gradient[0], gradient[1])
    strip.show()
    begin += 1
    time.sleep(0.1)
    strip.clear()
    strip.set_pixel_line_gradient(begin, end, gradient[0], gradient[1])
    strip.show()

# ALWAYS USE STRIP.SHOW()!!!!!!!!!

def expand():
    global end, begin
    end += 1
    time.sleep(0.1)
    strip.clear()
    strip.set_pixel_line_gradient(begin, end, gradient[0], gradient[1])
    strip.show()
    end += 1
    time.sleep(0.1)
    strip.clear()
    strip.set_pixel_line_gradient(begin, end, gradient[0], gradient[1])
    strip.show()
    if end > pixels:
        begin = 0
        end = 5

expand_timer = Timer()
contract_timer = Timer()

contract_timer.init(period=500, mode=Timer.PERIODIC, callback=lambda t: contract())
time.sleep(0.25)
expand_timer.init(period=500, mode=Timer.PERIODIC, callback=lambda t: expand())
