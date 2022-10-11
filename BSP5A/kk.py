from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import mysql.connector as mysql
class unit:
    def ShowData():
        con = mysql.connect(host='localhost', user='root', password='',
                            database='BSP5A')
        cursor = conn.cursor()
        cursor.execute('select * from tbunit')
        result = cursor.fetchall()

    if (len(result) != 0)
        self.member_record.delete(*self.member_record.get_chilldren())
        for row in result:
            self.member_record.insert('', END, value=row)
            cursor.execute('conmit')
            conn.close()
    def    SaveData():
        con = mysql.connect(host='localhost', user='root', password='',
                            database='BSP5A')
        cursor.execute('Insert into tbunit values(%s.%s)',
                    )(unitid.get(),unitname.get())


