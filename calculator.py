from tkinter import *
import math
root=Tk()
root.title("manas calculator")
e=Entry(root,borderwidth=10,width=20)
m=e.get()
e.grid(row=0,column=0,columnspan=3)

def button_add():
    f_num=e.get()
    global first
    global manas
    manas="addition"
    e.delete(0,END)
    first=float(f_num)
def button_sub():
    f_num=e.get()
    global first
    global manas
    manas="subtraction"
    e.delete(0,END)
    first=float(f_num)
def button_mull():   
    f_num=e.get()
    global first
    global manas
    manas="multiplication"
    e.delete(0,END)
    first=float(f_num)
def button_div():
    f_num=e.get()
    global first
    global manas
    manas="division"
    e.delete(0,END)
    first=float(f_num)
def button_clear():
    e.delete(0,END)
def button_dot():
    present = e.get()
    if '.' not in present:
        e.delete(0, END)
        e.insert(0, present + '.')
    manas="dot"
def button_press(num):
    present=e.get()
    e.delete(0,END)
    e.insert(0,str(present)+str(num))
def button_equal():
    s_num=e.get()
    e.delete(0,END)
    if manas=="addition":
        e.insert(0,first+float(s_num))
    if manas=="subtraction":
        e.insert(0,first-float(s_num))
    if manas=="multiplication":
        e.insert(0,first*float(s_num))
    if manas=="division":
        e.insert(0,first/float(s_num))
    if manas=="dot":
        e.insert(0,first + "." )

button1=Button(root,text="1",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(1))
button2=Button(root,text="2",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(2))
button3=Button(root,text="3",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(3))
button4=Button(root,text="4",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(4))
button5=Button(root,text="5",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(5))
button6=Button(root,text="6",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(6))
button7=Button(root,text="7",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(7))
button8=Button(root,text="8",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(8))
button9=Button(root,text="9",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(9))
button0=Button(root,text="0",padx=40,pady=20,bg="#58FC00",command=lambda:button_press(0))
button_add=Button(root,text="+",padx=40,pady=20,bg="#58FC00",command=button_add)
button_sub=Button(root,text="-",padx=40,pady=20,bg="#58FC00",command=button_sub)
button_mull=Button(root,text="*",padx=40,pady=20,bg="#58FC00",command=button_mull)
button_div=Button(root,text="/",padx=40,pady=20,bg="#58FC00",command=button_div)
button_dot=Button(root,text=".",padx=41,pady=20,bg="#58FC00",command=button_dot)
button_equal=Button(root,text="=",padx=40,pady=20,bg="#58FC00",command=button_equal)
#button_fdi=Button(root,text="%",padx=40,pady=20,bg="#58FC00",command=button_fdi)
button_clear=Button(root,text="Clear",padx=30,pady=20,bg="#58FC00",command=button_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=3,column=3)
button_sub.grid(row=2,column=3)
button_mull.grid(row=1,column=3)
button_div.grid(row=0,column=3)
button_dot.grid(row=4,column=1)
button_equal.grid(row=4,column=3)
#button_fdi.grid(row=0,column=2)
button_clear.grid(row=4,column=2)
button0.grid(row=4,column=0)

root.mainloop()