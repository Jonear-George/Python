from tkinter import*
import tkinter.messagebox as Msg
def Bnk():
    if bath.get()=='':
        Msg.showinfo("infor", "Enter bath please!!!", icon='warning')
        txt1.focus_set()
    elif rate.get()=='':
        Msg.showinfo("nfor", "Enter bath please!!!", icon='warning')
        txt2.focus_set()
    elif bath.get():
        Msg.showinfo("infor", "Enter bath is number only please!!!", icon='warning')
        txt1.focus_set()
    else:
        b = int(bath.get())
        r = int(rate.get())
        k = b * r
        kip.set(f'{k:,}kip')
def allclear():
    bath.set('')
    rate.set('')
    kip.set('')

root = Tk()
root.title("Hello Python")
root.geometry('500x500')
bath=StringVar()
rate=StringVar()
kip=StringVar()



lb1=Label(root,font=('Phetsarath OT',16),text='ແລກປ່ຽນ')
lb1.place(x=200,y=50)
lb2=Label(root,font=('Times new Roman',16),text='Enter Bath')
lb2.place(x=50,y=100)

lb3=Label(root,font=('Times new Roman',16),text='Enter Rate')
lb3.place(x=50,y=150)
lb4=Label(root,font=('Times new Roman',16),text='Total')
lb4.place(x=50,y=300)

text1=Entry(root,font=('Times new Roman',16),textvariable=bath)
text1.place(x=150,y=100)
text3=Entry(root,font=('Times new Roman',16),textvariable=kip)
text3.place(x=150,y=300)
text2=Entry(root,font=('Times new Roman',16),textvariable=rate)
text2.place(x=150,y=150)

btn1=Button(root,font=('Time New Roman',16), text ='Exchange',command=Bnk)
btn1.place(x=150, y=200)
btn2=Button(root,font=('Time New Roman',16), text ='Clear',command=allclear)
btn2.place(x=300, y=200)
root.mainloop()