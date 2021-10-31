import serial
import time

sp= serial.Serial(
    port='/dev/ttyAMA0',
    baudrate= 115200,
    timeout=1)

sp.write("AT+CUSD=1,\"*124#\",15\r".encode('utf-8'))
bal=''
while True:
    response = sp.readline()
    print(response)
    if b'+CUSD:' in response:
        balance = response.decode('utf-8')