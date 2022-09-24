from tkinter import *
from tkinter import messagebox
from db import config
import sqlite3



db = config('book.db')
def dply():
    dbbox.delete(0, END)
    for row in db.fetch():
        dbbox.insert(END, row)
def add():
    if namebtxt.get() == '' or customer_text.get() == '' or timetxt.get() == '' or endatetxt.get() == '':
        messagebox.showerror('ใส่ให้ครบ', 'กรุณาเติมให้ครบ')
        return
    db.insert(namebtxt.get(), customer_text.get(),timetxt.get(), endatetxt.get())
    dbbox.delete(0, END)
    dbbox.insert(END, (namebtxt.get(), customer_text.get(),timetxt.get(), endatetxt.get()))
    clstxt()
    dply()

def sct(event):
    try:
        global selected_item
        index = dbbox.curselection()[0]
        selected_item = dbbox.get(index)
        namebconfig.delete(0, END)
        namebconfig.insert(END, selected_item[1])
        nameconfig.delete(0, END)
        nameconfig.insert(END, selected_item[2])
        dateconfig.delete(0, END)
        dateconfig.insert(END, selected_item[3])
        endateconfig.delete(0, END)
        endateconfig.insert(END, selected_item[4])
    except IndexError:
        pass


def rm():
    db.remove(selected_item[0])
    clstxt()
    dply()
def upt():
    db.update(selected_item[0], namebtxt.get(), customer_text.get(),
              timetxt.get(), endatetxt.get())
    dply()


def clstxt():
    namebconfig.delete(0, END)
    nameconfig.delete(0, END)
    dateconfig.delete(0, END)
    endateconfig.delete(0, END)


app = Tk()

namebtxt = StringVar()
nameblb = Label(app, text='ชื่อหนังสือ', font=('Courier', 23), pady=20)
nameblb.grid(row=0, column=0)
namebconfig = Entry(app, textvariable=namebtxt)
namebconfig.config(font=("Courier", 17))
namebconfig.grid(row=0, column=1)
# ส่วนคนยืม 
customer_text = StringVar()
nameclb = Label(app, text='ชื่อคนยืม', font=('Courier', 23))
nameclb.grid(row=0, column=2, sticky=W)
nameconfig = Entry(app, textvariable=customer_text)
nameconfig.config(font=("Courier", 17))
nameconfig.grid(row=0, column=3)
# ส่วนของเวลา
timetxt = StringVar()
timelb = Label(app, text='วันที่เช่า', font=('Courier', 23), pady=20)
timelb.grid(row=1, column=0, sticky=W)
dateconfig = Entry(app, textvariable=timetxt)
dateconfig.config(font=("Courier", 17))
dateconfig.grid(row=1, column=1)
#--------------------------------#
endatetxt = StringVar()
endatelb = Label(app, text='วันที่สิ้นสุดการยืม', font=('Courier', 23))
endatelb.grid(row=1, column=2, sticky=W)
endateconfig = Entry(app, textvariable=endatetxt)
endateconfig.config(font=("Courier", 17))
endateconfig.grid(row=1, column=3)

dbbox = Listbox(app, height=10, width=100, border=5)
dbbox.grid(row=5, column=0, columnspan=3, rowspan=6, pady=30, padx=20)

sc = Scrollbar(app)
sc.grid(row=3, column=3)
dbbox.configure(yscrollcommand=sc.set)
sc.configure(command=dbbox.yview)

dbbox.bind('<<ListboxSelect>>', sct)

add = Button(app, text='เพิ่มชื่อ', width=12, command=add)
add.grid(row=3, column=0, pady=20)
add.config(font=("Courier", 20), border=5)
clear = Button(app, text='เคลียร์ช่อง', width=12, command=clstxt)
clear.grid(row=3, column=1)
clear.config(font=("Courier", 20), border=5)
remove = Button(app, text='เอารายชื่อออก', width=12, command=rm)
remove.grid(row=3, column=2)
remove.config(font=("Courier", 20), border=5)
update = Button(app, text='เเก้ไข', width=12, command=upt)
update.grid(row=3, column=3)
update.config(font=("Courier", 20), border=5)
app.title('Book Borrow management ')
app.geometry('1000x470')
app.resizable(False, False)
dply()


app.mainloop()



