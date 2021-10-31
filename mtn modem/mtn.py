import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyUSB2",
    baudrate=9600,
    timeout=1)


#debug message
'''print('resetting....')
#synchronizing baud rate and transmiting AT
sp.write('ATZ\r'.encode('utf-8'))
rspn = sp.readline()
print(rspn.decode('utf-8'))
time.sleep(2)'''

#debug message
print('transmiting CMGF....')
#synchronizing baud rate and transmiting AT
sp.write('AT+CMGF=1\r'.encode())
#synchronised=''
rspn = sp.readline()
print(rspn.decode())
time.sleep(2)


#debug message
print('transmiting At....')
#synchronizing baud rate and transmiting AT
sp.write('AT\r'.encode('utf-8'))
#synchronised=''
rspn = sp.readline()
print(rspn.decode('utf-8'))
time.sleep(2)
    
#setting USSD to 1 //(turing on)
'''sp.write('AT+CUSD=1'.encode())
resp = sp.read(10)
time.sleep(1)
print(resp.decode('utf-8'))'''

#debug message
print('checking balance...')
#atcmd=
'''sp.write("AT+CUSD=1,\"*124#\",15\r".encode())
#response = sp.read(sp.in_waiting)567
res = ''
while True:
    print('reading response in input buffer...')
    response = sp.readline()
    print(response)
    if b'+CUSD:2' in response:
        res = response.decode()
        break'''
    
#checking balance
sp.write("AT+CUSD=1,\"*124#\",15\r".encode('utf-8'))
bal=''
while True:
    response = sp.readline()
    time.sleep(2)
    print(response)
    if b'+CUSD:' in response:
        balance = response.decode('utf-8')
        break
     