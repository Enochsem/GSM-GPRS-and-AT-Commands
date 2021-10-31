import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyUSB2",
    baudrate=9600,
    timeout=1)

#debug message
print('transmiting At....')
#synchronizing baud rate and transmiting AT
sp.write('AT\r'.encode('utf-8'))
synchronised=''
while True :
    rspn = sp.readline()
    print(rspn.decode('utf-8'))
    if b'OK' in rspn:
        synchronised=rspn
        break
        
    
    
'''
#setting DEC baud rate to DTE 
sp.write('AT+IPR'.encode())
#rspn = sp.read(10)
#print(rspn.decode('utf-8'))
#time.sleep(1)
time.sleep(4)
while True :
    rspn = sp.read(10)
    print(rspn.decode())
    break
    '''
    
#setting USSD to 1 //(turing on)
#sp.write('AT+CUSD=1'.encode())
#resp = sp.read(10)
#time.sleep(1)

#debug message
print('checking balance...')
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
        