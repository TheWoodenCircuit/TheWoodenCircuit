from digitalio import DigitalInOut, Direction
import board

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

led.value = True