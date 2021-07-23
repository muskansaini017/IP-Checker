# IP Address Checker is a desktop-application to check IP Address.

import tkinter
from tkinter import messagebox
from tkinter import *

# creating functions
def get_IP():
    global IP_raw, IP
    IP=entry1_var.get()
    checkpoint1_IP()

def checkpoint1_IP():
    if len(IP)<=15:
        checkpoint2_IP()
    else:
        messagebox.showinfo("IP Checker", "Your IP is not Valid")

def checkpoint2_IP():
    slots=list(IP.split('.'))
    if(len(slots)==4):
        a=0
        for e in slots:
            data=int(e)
            if(data<=255):
                a=a+1
                if(a>=4):
                    messagebox.showinfo("IP Checker","Your IP is Valid")
                    break
            else:
                messagebox.showinfo("IP Checker", "Your IP is not Valid")
    else:
        messagebox.showinfo("IP Checker", "Your IP is not Valid")
#def clear():



# creating window
window= tkinter.Tk()
window.title("My IP Address Checker Desktop Application")
window.configure(background='Cadet Blue')
window.geometry("400x350+450+150")
window.resizable(0,0)

# creating frame
frame1= Frame(window,bg='Cadet Blue')
frame1.pack()

frame2= Frame(window,bg='Cadet Blue')
frame2.pack()

frame3= Frame(window,bg='Cadet Blue')
frame3.pack(expand=True, fill= "both")

# creating labels
lable1=Label(frame1,text='IP ADDRESS CHECKER',font=("Verdana Bold",20),bg='Cadet Blue')
lable1.pack(pady=20)

lable2=Label(frame1,text='Note :- Please enter the IP Address below in the box.\n'
                         '(Only for IPv4)',font=("Verdana",9),bg="Cadet Blue")
lable2.pack()

lable3=Label(frame2,text="IP is known as Internet Protocol.\n"
                         "It is a numerical label assigned to each\n"
                         "device connected to a computer network.",
                        font=("Verdana Bold Italic",10),bg='Cadet Blue')
lable3.pack(pady=20)


# creating Entry
entry1_var=StringVar()
entry1=Entry(frame2, width=45, textvariable=entry1_var)
entry1.pack()
entry1.focus()

# creating buttons
click=Button(frame3,width=10,text='Check',bg="Blue",fg='White',
             font=("Verdana Bold",10),relief=GROOVE,command=get_IP)
click.pack(pady=20)

window.mainloop()
