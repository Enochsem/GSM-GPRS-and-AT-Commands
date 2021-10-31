import serial
import time

sp = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    timeout=1)

def sychronize():
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



def serviceContact():
    #accessing service center number
    sp.write('AT+CSCA?\r'.encode())
    while True :
        rspn = sp.readline()
        print(rspn)
        if b'+CSCA' in rspn:
            rcv=rspn.decode('utf-8')
            print('current number:'+str(rcv[8:18]))

def modelID():
    sp.write('AT+GMM\r'.encode('utf-8'))
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))


def makeCall(number):
    atcmd='ATD{};'.format(number)
    sp.write(atcmd.encode('utf-8'))
    response=sp.readline()
    time.sleep(4)
    while (1):
        response=sp.readline()
        #print(response)
        if b' ' in response:
            continue
            #response=sp.readline()
            #confirmed=response.decode('utf-8')
        else:
            print(response)
            
        
    
def answerCall():
    atcmd='ATA'
    sp.write(atcmd.decode('utf-8'))
    while True:
        response=sp.readline()
        print(response)
        if b'OK' in response:
            confirmed=response.decode('utf-8')
            break


        
#num=input('enter number\n')
        
#makeCall('0554317909')