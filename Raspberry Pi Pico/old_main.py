import machine
#from pico_i2c_lcd import I2cLcd
#import utime

#from ht16k33segmentbig import HT16K33SegmentBig

def zfl(s, width):
    return '{:0>{w}}'.format(s, w=width)




"""
led = machine.Pin("LED", machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def refresh_lcd(t):
    time = utime.localtime()
    #lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(zfl(str(time[3]), 2) + ":" + zfl(str(time[4]), 2) + ":" + zfl(str(time[5]), 2))
    if display_balls:
        lcd.putstr("balls")

def check_btn(t):
    global t2_counter
    t2_coun
    if t.counter() > 500 and btn.value():
        display_balls = not display_balls
        lcd.clear()
        #time_of_last_toggle = ct



t2 = machine.Timer()
t2.init(mode=machine.Timer.PERIODIC, freq=10, callback=check_btn)
t2_time_of_exec = 0
"""
"""
t1 = machine.Timer()
t1.init(mode=machine.Timer.PERIODIC, freq=1, callback=4refresh_lcd)
"""

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=400000)

led = HT16K33SegmentBig(i2c)

led.clear()#.set_number(4, 0).set_number(3, 1).draw()