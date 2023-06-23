import neopixel
import board
import time

pixels = 280
strip = neopixel.NeoPixel(board.GP28, pixels, brightness=0.3, auto_write=False)


# This can be replaced with other gradients or colors
red = (255, 0, 0)
black = (0, 0, 0)

begin = 0
end = 5


def fill_line(p1, p2, color):
    for i in range(p1, p2):
        strip[i] = color
def clear():
    strip.fill(black)

def contract():
    global begin
    begin += 1
    time.sleep(0.1)
    clear()
    fill_line(begin, end, red)
    strip.show()
    begin += 1
    time.sleep(0.1)
    clear()
    fill_line(begin, end, red)
    strip.show()

# ALWAYS USE STRIP.SHOW()!!!!!!!!!

def expand():
    global end, begin
    if end + 2 > pixels:
        begin = 0
        end = 5
    end += 1
    time.sleep(0.1)
    clear()
    fill_line(begin, end, red)
    strip.show()
    end += 1
    time.sleep(0.1)
    clear()
    fill_line(begin, end, red)
    strip.show()

while True:
    expand()
    contract()


