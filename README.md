# The Wooden Circuit
**This repository contains example code for The Wooden Circuit projects**

This readme is divided into the different hardware that the code can be used for, and explains how to upload and install those programs onto the device.

## Raspberry Pi Pico with adafruit-ampy

**If you want to use an IDE to run your MicroPython code, check out [Thonny](https://thonny.org) and its tutorial [here](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico/micropython-installation).**

**General Prerequisites**
`adafruit-ampy` *Install via Python PIP* `pip3 install adafruit-ampy`   
Raspberry Pi Pico set up with MicroPython firmware

**macOS and Linux Instructions**
1. Open a terminal
2. Ensure that `ampy` is in your `PATH`  
3. Plug in your Raspberry Pi Pico to your computer. 
4. To check what device port your Pico is connected to, type the command `ls /dev/tty*`. This will list all TTY ports on your computer. While different computers or operating systems might have different port systems, look for something with `usb` or `modem` in it.
5. Copy that path and run the following command: `ampy --port <PASTE PATH> ls`. This lists the files on your Pico (no result means that you don't have any files stored.)
6. Download the MicroPython file you want from this repository or wherever it is stored
7. Rename the file to `main.py` to ensure it functions correctly on the Pico
8. Ensure you're in the same directory as the file and run the command: `ampy --port <PASTE PORT> put main.py`
9. To finally run the file, `ampy --port <PASTE PORT> run main.py`
