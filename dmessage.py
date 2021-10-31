import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    timeout=1)



#debug message
print('transmiting At....')
#synchronizing baud rate and transmiting AT
sp.write('AT\r'.encode('utf-8'))
synchronised=''
while True :
    rspn = sp.readline()
    print(synchronised)
    if b'OK' in rspn:
        synchronised=rspn.decode('utf-8')
        break




'''
sp.write("AT+CPIN?\r".encode('utf-8'))
while True :
    rspn = sp.readline()
    print(rspn)
    if b'OK' in rspn:
        confirmed=rspn.decode('utf-8')
        break'''

def sendmsg(recipient,message):
    #seting sms format to 1 
    atcmd="AT+CMGF=1\r"
    sp.write(atcmd.encode('utf-8'))
    while True:
        response=sp.readline()
        print(response)
        if b'OK' in response:
            confrimed=response.decode('utf-8')
            break
        

   #setting recipient and writing message             
    atcmd="AT+CMGS=\"{}\"\r".format(recipient)
    sp.write(atcmd.encode('utf-8'))
    time.sleep(1)
    sp.write(message.encode('utf-8'))
    time.sleep(1)
    sp.write('\x1A'.encode())
    while True :
        rspn = sp.readline()
        if b'+CMGS' in rspn or b'OK' in rspn:
            confrimed=rspn.decode('utf-8')
            #debug msg
            print(confrimed)
            print("Message sent to {} successfully".format(message))
            break
        
        
'''
recipient=str(input('Enter recipient contact\n'))
message=str(input('Enter message\n'))
'''
sendmsg('0540229000','hello from mtn sim800c')
