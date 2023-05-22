# This code is designed for the Raspberry Pi Pico W. Any differences in code to be noted will be commented

from machine import Pin, Timer

led = Pin("LED") # For use on a regular Pico, replace "LED" with pin number 25

t = Timer()
t.init(mode=Timer.PERIODIC, freq=1.5, callback=lambda t: led.toggle())