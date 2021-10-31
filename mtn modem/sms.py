import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=9600,
    timeout=1)



#debug message
print('transmiting At....')
#synchronizing baud rate and transmiting AT
sp.write('AT\r'.encode('utf-8'))
#synchronised=''
rspn = sp.readline()
print(rspn.decode('utf-8'))
time.sleep(2)

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
    sp.write(atcmd.encode())
    time.sleep(1)
    sp.write(message.encode())
    time.sleep(1)
    sp.write('\x1A'.encode())
    while True :
        rspn = sp.readline()
        if b'+CMGS' in rspn or b'OK' in rspn:
            confrimed=rspn.decode()
            #debug msg
            print(confrimed)
            print("Message sent to {} successfully".format(recipient))
            break
        
        
'''
recipient=str(input('Enter recipient contact\n'))
message=str(input('Enter message\n'))0540229000
'''
sendmsg('0554317909','hello from mtn')
