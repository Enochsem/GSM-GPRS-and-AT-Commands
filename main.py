#import serial
#import time
from balance import checkBalance
from message import Message
from call import *
from net import *


'''    
sp= serial.Serial(
    port='/dev/ttyAMA0',
    baudrate= 115200,
    timeout=1)'''



#menu
def menu():
    print(
        '1.Get balance\n'+
        '2.Send message\n'+
        '3.Service contact\n'+
        '4.Model identification\n'+
        '5.Check Transmition\n'+
        '6.Make a call\n'
        )
    
def getBalance():
    code=str(input('Enter pin code'))
    #debuge message 
    print('Get balance')
    checkBalance(code)
    
    
def sendmsg():
    rcpt=str(input('Enter recipient number'))
    msgcnt=str(input('Enter message'))
    msg=Message(rcpt,msgcnt)
    msg.setTextMode()
    msg.sendMessage()
    

        

while True:
    menu()
    #taking user input
    choice= str(input('Make a choice: '))
    if choice == '1':
        #Get balance
        getBalance()
    elif choice == '2':
        #Send Message
        print('Required Details')
        sendmsg()
    elif choice == '3':
        #Service contact
        print('Service contact')
        serviceContact()
    elif choice == '4':
        #Model identification
        print('Model identification')
        modelID()
    elif choice == '5':
        #Check Transmition
        sychronize()
    elif choice == '6':
        #Make a call
        number=str(input('\tEnter recipient contact\t'))
        makeCall(number)
    else:
        print('invalid input')