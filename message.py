import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    timeout=1)

class Message:
    
    def __init__(self,recipient,message):
        self.recipient=recipient
        self.message=message
     
     #seting sms format to 1
    def setTextMode(self):
        atcmd="AT+CMGF=1\r"
        sp.write(atcmd.encode('utf-8'))
        while True:
            response=sp.readline()
            print(response)
            if b'OK' in response:
                confrimed=response.decode('utf-8')
                break
    
    def sendMessage(self):
        atcmd="AT+CMGS=\"{}\"\r".format(self.recipient)
        sp.write(atcmd.encode('utf-8'))
        time.sleep(1)
        sp.write(self.message.encode('utf-8'))
        time.sleep(1)
        sp.write('\x1A'.encode())
        while True :
            rspn = sp.readline()
            if b'+CMGS' in rspn or b'OK' in rspn:
                confrimed=rspn.decode('utf-8')
                #debug msg
                if confirmed :
                    print("Message sent to {} successfully".format(self.recipient))
                    break
            else:
                print('waiting..')
        
        
