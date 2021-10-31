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
        

#turning flow control on (effective communication)
'''atCmd=bytes('AT+IFC','utf-8')
sp.write(atCmd)
rspn = sp.read(10)
print(rspn.decode('utf-8'))'''


def str2byte(string):
    return bytes(string,'utf-8')

def byte2str(b):
    print(b.decode('utf-8'))
   

def sendmsg(recipient,message):
    #confirm=''
    #seting sms text mode parameters
    sp.write('AT+CSMP=17,167,0,0\r'.encode('utf-8'))
    while True :
        rspn = sp.readline()
        print(rspn)
        if b'OK' in rspn:
            confirm=rspn.decode('utf-8')
            break
        
    #Setting show text parameters to 1(visible)
    sp.write('AT+CSDH=1\r'.encode('utf-8'))
    while True :
        rspn = sp.readline()
        print(rspn) #if rspn not '' else pass
        if b'OK' in rspn:
            confirm=rspn.decode('utf-8')
            break
    
    
    #accessing service center number
    sp.write('AT+CSCA?\r'.encode())
    while True :
        rspn = sp.readline()
        print(rspn)
        if b'+CSCA' in rspn:
            rcv=rspn.decode('utf-8')
            print('current number:'+str(rcv[8:18]))
            time.sleep(2)
            #seting sms format to 1 along side the +csca
            atcmd="AT+CSCA=\"{}\";+CMGF=1\r".format(rcv)
            sp.write(atcmd.encode('utf-8'))
            while True:
                confrim=sp.readline()
                print(confrim)
                if 'OK' in confirm:
                    confrimed=confirm.decode('utf-8')
                    break
                    
    
    #seting new message indicators and saving sms settings
    sp.write('AT+CNMI?\r'.encode())
    while True :
        rspn = sp.readline()
        print(rcv)
        if b'+CNMI' in rspn:
            rcv=rspn.decode('utf-8')
            print('current indicator:'+str(rcv[8:17]))
            #saving sms settings to profile 1 along side the +
            atcmd='AT+CNMI={};+CSAS=1\r'.format(rcv)
            sp.write(atcmd.encode('utf-8'))
            while(1):
                confrim=sp.readline()
                if b'OK' in confirm:
                    confrim=confim.decode('utf-8')
                    print(confrim)
                    break
   
   #setting recipient and writing message             
    atcmd='AT+CMGS=\'{}\'\r'.format(recipient)
    sp.write(atcmd.encode('utf-8'))
    time.sleep(1)
    sp.write(message.encode('utf-8'))
    time.sleep(1)
    sp.write('\x1A'.encode())
    while True :
        rspn = sp.readline()
        if b'Ok' in rspn or b'Error' in rspn:
            confirm=rspn.decode('utf-8')
            #debug msg
            print(confirm)
            break
        
        
    
    
    '''
    atcd=str2byte('AT+CSCA=')
    mycnct=str2byte('mycnct')
    sp.write(atcd+mycnct)
    respn = sp.readline()
    print(respn.decode('utf-8'))'''
    
    '''atcd=str2byte('AT+CMGS=')
    yrcnct=str2byte('yrcnct')
    sp.write(atcd+mycnct)
    respn = sp.readline()
    print(respn.decode('utf-8'))
    
    sp.write('\x1A'.encode())
    respn = sp.readline()
    print(respn.decode('utf-8'))'''


'''
recipient=str(input('Enter recipient contact\n'))
message=str(input('Enter message\n'))
'''
sendmsg('0239594309','hello from sim800c')