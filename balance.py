import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    timeout=1)

global bal

#synchronizing baud rate
sp = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    timeout=1)

#debug message
'''
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

#turning flow control on (effective communication)
'''atCmd=bytes('AT+IFC','utf-8')
sp.write(atCmd)
rspn = sp.read(10)
print(rspn.decode('utf-8'))'''


def str2byte(s):
    return bytes(s,'utf-8')

def byte2str(b):
    print(b.decode('utf-8'))
   
def checkBalance(code) :
    #first enable USSD
    '''atcmd=str2byte('AT+CUSD=1')
    sp.write(atcmd)
    resp = sp.read(10)
    time.sleep(1)'''
    
    #checking balance
    atcd="AT+CUSD=1,\"*{}#\",15\r".format(code)
    sp.write(atcd.encode('utf-8'))
    bal=''
    while True:
        response = sp.readline()
        time.sleep(2)
        print(response)
        if b'+CUSD:' in response:
            balance = response.decode('utf-8')
            break
           
if __name__ =="__main__":
    code=str(input('Enter code to check account balance\n'))

    checkBalance(code)
