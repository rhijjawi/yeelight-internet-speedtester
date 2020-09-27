from yeelight import LightType
from yeelight import Bulb
import time
import speedtest
bulbleft = Bulb("192.168.x.x", effect="sudden", duration=1000, auto_on=True) #Bulb on the left side of the kitchen. This will be used for upload speeds
bulbright = Bulb("192.168.x.x", effect="sudden", duration=1000, auto_on=True) #Bulb on the right side of the kitchen. This will be used for download speeds 
bulbright.effect = "sudden"
bulbleft.effect = "sudden"
servers = []
def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]
d, u, p = test()
dkbps = d / 1024
dmbps = dkbps / 1024
ukbps = u / 1024
umbps = ukbps / 1024
bulbright.turn_on()
bulbleft.turn_on()
print(f'Download speed un-rounded and rounded:\n{dmbps}')
print(round(dmbps))
print(f'Upload speed un-rounded and rounded:\n{umbps}')
print(round(umbps))
if 0 < dmbps < 2: #If download speed is below 2mbps, set the bulb color to red.
    bulbright.set_rgb(255, 0, 0)

if 2 < dmbps < 5: #If download speed is between 2 and 5mbps, set the bulb color to yellow.
    bulbright.set_rgb(255, 255, 0)

if 5 < dmbps: #If upload speed is greater than 5mbps, set the bulb color to green.
    bulbright.set_rgb(0, 255, 0)


if 0 < umbps < 2: #If upload speed is below 2mbps, set the bulb color to red.
    bulbleft.set_rgb(255, 0, 0)

if 2 < umbps < 5: #If upload speed is between 2 and 5mbps, set the bulb color to yellow.
    bulbleft.set_rgb(255, 255, 0)

if 5 < umbps: #If upload speed is greater than 5mbps, set the bulb color to green.
    bulbleft.set_rgb(0, 255, 0)
time.sleep(20) #Reset bulbs to normal color temperature after X seconds
bulbright.set_color_temp(3500)
bulbleft.set_color_temp(3500)
