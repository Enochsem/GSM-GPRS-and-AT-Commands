def enterBttonclick():
    global number
    global kblabel
    #e.insert(0,'\r\n')
    
    for i in displayButtons:
        i.grid_forget()
    display.grid_forget()
    global menu
    kbdisplay = LabelFrame(root, padx=80, pady=5, bg='white')
    kbdisplay.grid(row=0, column=0, padx=1, pady=1, columnspan=6)
    
    kblabletitle = Label(kbdisplay,fg='black', text='To: ', padx=1, pady=1)
    kblabletitle.grid(row=1, column=0, columnspan=2)
    
    kbe = Entry(kbdisplay,width=15, borderwidth=5)
    kbe.grid(row=1, column=2, columnspan=4, padx=10, pady=10)
    kbe.focus()
    global contact 
    contact= kbe.get()
    
    
    kblabel = Label(kbdisplay, bg='white', text=menu, padx=5, pady=5)
    kblabel.grid(row=2, column=0, columnspan=6)
    
    newkeyboard=[]
    btns=[
        'q','w','e','r','t','y','u','i','o','p'
        ,'a','s','d','f','g','h','j','k','l'
        ,'z','x','c','v','b','n','m','@','#','%','*','+','-','=','.','?'
        ,'enter','space','clear','123','send'
          ]
    row = 3
    col= 0
    #for i in btns:
    x=5
    y=5
    for btn in btns:
        cmd = lambda x = btn:click(x)
        Btns=Button(root, text=btn, padx=x, pady=y,width=5,height=1 ,command=cmd)
        displayButtons.append(Btns)
        displayButtons[-1].grid(row=row, column=col,columnspan=len(btn))
        col+=1
        if col == 6:
            row+=1
            col=0
