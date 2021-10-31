#from main import *
import serial
import time
from tkinter import *


sp= serial.Serial(port='/dev/ttyAMA0',baudrate= 115200,timeout=1)
'''
'''

root = Tk()
root.title('Nokia')
number = ''
contact = ''
def click(btn):
    print(str(btn))
    global number
    global kblabel
    global contact
    
    label['width']=28
    label['height']=8
    
    if btn == 'send':
        label['width']=30
        if len(number) == 5 and '*' in number and '#' in number:
            label['text']='USSD code runing ...'
            balance(number)
           
        elif len(number) == 10 or len(number) == 12:
            label['text']='calling '+str(number)+'...'
            makeCall(number)
            
        elif number.isalpha() and isinstance(number, str):
            #call the message function
            if len(number) == 10 or len(number) == 12 and contact != '':
                message = number
                sendmsg(contact,message)
            print('message')
            
        else:
            label['text']='calling....'
            time.sleep(1)
            label['text']='invalid number'
            label['fg']='red'
           
    elif btn == 'clear':
        clearButtonclick()
    
    elif btn == 'msg':
            to = Label(display,fg='black', text='To: ', padx=1, pady=1)
            to.grid(row=2, column=0, columnspan=2)
            
            toE = Entry(display,width=15, borderwidth=5)
            toE.grid(row=2, column=2, columnspan=4, padx=10, pady=10)
            toE.focus()
            
            
            if contact != '':
                sendmsg(contact, number)
        
    elif btn == 'abc':
        enterBttonclick()
    else:
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(btn))
        number=e.get()
        label['text']=number
        
        #kblabel['height']=8
        #kblabel['width']=18
        #kblabel['text']=number
        #label['text']=number
        e.delete(1,END)
        e.insert(1,str(current)+str(btn))
        contact=toE.get()
    
    
        
def enterBttonclick():
    pass


    
    
def clearButtonclick():
    e.delete(0,END)
    current=e.get()
    global menu
    label['text']=menu


def balance(code):
    atCommand ="AT+CUSD=1,\"{}\",15\r".format(code)
    sp.write(atCommand.encode('utf-8'))
    while True:
        response = sp.readline()
        print(response)
        if b'+CUSD:' in response:
            balance = response.decode('utf-8')
            str(balance)
            binary, data = balance.split('"',1)
            v,i = data.split(',',1)
            print(str(v)+'\n'+str(i))
            label['text']= str(v)+'\n'+str(i)
            break


def makeCall(number):
    atcmd='ATD{};\r'.format(number)
    sp.write(atcmd.encode('utf-8'))
    response=sp.readline()
    #time.sleep(4)
    response=sp.readline()
    
def endCall(number):
    atcmd='ATH\r'.format(number)
    sp.write(atcmd.encode('utf-8'))
    response=sp.readline()
    
    
def sendmsg(recipient,message):
    #seting sms format to 1 
    atcmd="AT+CMGF=1\r"
    sp.write(atcmd.encode('utf-8'))
    response=sp.readline()    
    time.sleep(0.5)
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
            prompt = "Message sent to {} successfully".format(recipient)
            print(prompt)
            kblabel['text']= prompt
            break

        




display = LabelFrame(root, padx=280, pady=5, bg= 'white')
display.grid(row=0, column=0, padx=5, pady=5, columnspan=14)

#menuItems=['1.Get balance','2.Send message','3.Service contact','4.Model identification','5.Check Transmition','6.Make a call\n']
menu='''
1.Get balance
2.Send message
3.Service contact
4.Model identification
5.Check Transmition
6.Make a call
'''
label = Label(display, bg='white', text=menu)
label.grid(row=1, column=0, columnspan=14)


e=Entry(root,width=25, borderwidth=5)
e.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
e.focus()
#e.insert(0, 'make a choice')
e.grid_forget()

displayButtons=[]
#['1','2','3','4','5','6','7','8','9','*','0','#','clear','abc','send']
buttons=[
'1','2','3','4','5','6','7','8','9','*','0','#','abc','send'
,'Tab','q','w','e','r','t','y','u','i','o','p','{','}','|'
,'Caps','a','s','d','f','g','h','j','k','l',':','"',';','clear'
,'shift','z','x','c','v','b','n','m','@',',','%','?','+','-'
,'msg','enter','space','=','.','<','>'
]
row = 3
col= 0
x=0
y=0
for btn in buttons:
    cmd = lambda x = btn:click(x)
    Btns=Button(root, text=btn, padx=x, pady=y, width=5,height=1, command=cmd)
    displayButtons.append(Btns)
    displayButtons[-1].grid(row=row, column=col,columnspan=1)
    col+=1
    if col == 14:
        row+=1
        col=0



root.mainloop()
