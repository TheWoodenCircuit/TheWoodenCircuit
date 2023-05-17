"""
import network
import urequests
import utime
import machine


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Minstink", "draggie1975")

req = urequests.get("http://worldtimeapi.org/api/timezone/America/New_York").json()['unixtime'] - 18000
time = utime.localtime(req)
machine.RTC().datetime((time[0], time[1], time[2], time[6], time[3], time[4], time[5], 0))
"""