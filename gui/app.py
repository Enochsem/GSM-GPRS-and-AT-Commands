#from main import *
import serial
import time
from tkinter import *


sp= serial.Serial(port='/dev/ttyAMA0',baudrate= 115200,timeout=1)

number=''
def click(btn):
    print(str(btn))
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(btn))
    global number
    number=e.get()
    display['text']=number
    
    if btn == 'c':
        clearButtonclick()
    
    
def call():
    global number
    n=number
    atcmd='ATD{};'.format(n)
    sp.write(atcmd.encode('utf-8'))
    time.sleep(1)
    response=sp.readline()    
    display['text'] ='calling...'
    #response.decode('utf-8')
    print('calling...')


def endcall():
    atcmd='ATH;'
    sp.write(atcmd.encode('utf-8'))
    response=sp.readline()    
    display['text'] ='Call Ended'
    #response.decode('utf-8')
    


                
def balance():
    sp.write("AT+CUSD=1,\"*124#\",15\r".encode('utf-8'))
    bal=''
    while True:
        response = sp.readline()
        print(response)
        if b'+CUSD:' in response:
            balance = response.decode('utf-8')
            display['text']= balance
            break
        
                
        


def enterBttonclick():
    e.insert(0,'\r\n')
def clearButtonclick():
    e.delete(0,END)
    current=e.get()
    display['text']=current
    


root = Tk()

display = Label(root, text='', height=5, width=25, fg='black', bg='white')
display.grid(row=0, column=0, columnspan=3)



#balancBtn=Button(root, text='Balanc', padx=2, pady=2).grid(row=0, column=0)
callBtn=Button(root, text='call', padx=2, pady=2, command=balance)
callBtn.grid(row=0, column=2)
#endBtn=Button(root, text='bal', padx=2, pady=2, command=balance).grid(row=0, column=1)

e=Entry(root,width=30, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
e.grid_forget()

buttons=['1','2','3','4','5','6','7','8','9','*','0','#','c','e','s']
row = 2
col= 0
x=30
y=15
for btn in buttons:
    cmd = lambda x = btn:click(x)
    Button(root, text=btn, padx=x, pady=y, command=cmd).grid(row=row, column=col,columnspan=len(btn))
    col+=1
    if col == 3:
        row+=1
        col=0


root.mainloop()