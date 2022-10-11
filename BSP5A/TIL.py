from tkinter import*
import tkinter .messagebox as Msg
def Bank():
    if bath.get()=='':
        Msg.showinfo("infor","Enter bath please!!!",icon='warning')
        txt1.focus_set()
    elif rate.get()=='':
        Msg.showinfo("infor", "Enter bath please!!!", icon='warning')
        txt2.focus_set()
    elif bath.isalpha():
        Msg.showinfo("infor", "Enter bath is number only please!!!", icon='warning')
        txt1.focus_set()
    else:
        b=int(bath.get())
        r=int(rate.get())
        k=b*r
        kip.set(f'{k:,}kip')
def AllClear():
    bath.set('')
    rate.set('')
    kip.set("")

root = Tk()
root.title("Hello Python")
root.geometry('1240x800')
bath=StringVar()
rate=StringVar()
kip=StringVar()

Lb1=Label(root,font=('Time New Roman',16), text ='Bath to Kip')
Lb1.place(x=200, y=50)
Lb2=Label(root,font=('Time New Roman',16), text ='Enter Bath:')
Lb2.place(x=50, y=100)
Lb3 = Label(root, font=('Time New Roman', 16), text='Enter Rate:')
Lb3.place(x=50, y=150)
Lb4 = Label(root, font=('Time New Roman', 16), text='Total:')
Lb4.place(x=50, y=300)

txt1=Entry(root,font=('Time New Roman',16), textvariable=bath)
txt1.place(x=150, y=100)
txt2=Entry(root,font=('Time New Roman',16), textvariable=rate)
txt2.place(x=150, y=150)
txt3 = Entry(root, font=('Time New Roman', 16), textvariable=kip)
txt3.place(x=150, y=300)

btn1=Button(root,font=('Time New Roman',16), text ='Exchange',command=Bank)
btn1.place(x=100, y=200)
btn2=Button(root,font=('Time New Roman',16), text ='Clear',command=AllClear)
btn2.place(x=250, y=200)
root.mainloop()
