import socket
import time
import network
import transmitter_wifi

def run_secondary_script():
    print('Start Receiving....')
    transmitter_wifi.run()

wifi=network.WLAN(network.STA_IF)
time.sleep(.5)
wifi.active(True)
time.sleep(.5)
wifi.connect('Pixel_3a','jana99bandara')
cnt=0
while wifi.isconnected()== False:
    print('Waiting..........')
    time.sleep(1)
    cnt=cnt+1

wifiInfo=wifi.ifconfig()
print(wifiInfo)
ServerIp=wifiInfo[0]
print(ServerIp)
ServerPort=2222
bufferSize=1024
UDPServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServer.bind((ServerIp,ServerPort))
while True: 
    cmd, address =UDPServer.recvfrom(bufferSize)
    cmdDecoded=cmd.decode('utf-8')
    print(cmdDecoded)
    print('From: ', str(address[0]))
    if cmdDecoded == 'start':
        run_secondary_script()
