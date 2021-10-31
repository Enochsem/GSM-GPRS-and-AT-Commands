import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=115200,
    timeout=1)

#verifing that the sim is working
#sp.write('AT+CPIN?')
#shut all existing communication
#sp.write('AT+CIPSHUT')
#configure the divce for signal
#sp.write('AT+CIPMUX=0')

def connectTCP(host, port):
    cmd = 'AT+CIPSTART="TCP","' + host + '","' + str(port) + '"\r'
    sp.write(cmd.encode('utf-8'))
    time.sleep(5)
    reply = sp.read(sp.inWaiting())
    print(reply.decode('utf-8'))


def checkModermReg():
    #debug msg
    print('checking modem registration...')
    #check moderm registration to network carrier
    sp.write('AT+CREG?\r'.encode('utf-8'))
    time.sleep(3)
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))
    return response

def attachStatus():
    #debug msg
    print('checking attach status...')
    #checking attach status
    sp.write('AT+CGACT?\r'.encode())
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))
    
def attachNetwork():
    #debug msg
    print('attaching to network...')
    #attach to network
    sp.write('AT+CGACT=1\r'.encode())
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))
    time.sleep(1)    

def setAPN():
    #debug msg
    print('setting apn...')
    #attaching moderm to net carrier(APN)
    cmd = "AT+CSTT=\"internet\"\r"
    sp.write(cmd.encode('utf-8'))
    time.sleep(2)
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))
    
def enableWirelessConnt():
    #debug msg
    print('enabling wireless connection ...')
    # Bringing up network
    cmd = "AT+CIICR\r"
    sp.write(cmd.encode('utf-8'))
    time.sleep(2)
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))
    
def getLocalIP():
    #debug msg
    print('getting ip...')
    # Getting IP address
    cmd = "AT+CIFSR\r"
    sp.write(cmd.encode('utf-8'))
    time.sleep(3)
    response= sp.read(sp.in_waiting)
    print(response.decode('utf-8'))
    
    

#you can run this to complete the whole process
def checkAPN():
    #debug msg
    print('checking apn...')
    #attaching moderm to net carrier(APN)
    cmd = "AT+CSTT?\r"
    sp.write(cmd.encode('utf-8'))
    time.sleep(2)
    response= sp.read(sp.in_waiting)
    confirmed=response.decode('utf-8')
    while 'CMNET' in confirmed:
        setAPN()
        enableWirelessConnt()
        getLocalIP()
        connectTCP('youtube.com','80')
        


checkModermReg()
setAPN()
enableWirelessConnt()
getLocalIP()
connectTCP('youtube.com','80')
