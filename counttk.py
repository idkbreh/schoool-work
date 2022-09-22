from tkinter import *
root = Tk()

root.counter = 0

def clicked():
    root.counter += 1
    L['text'] = 'Order ที่ ' + str(root.counter)
b = Button(root, text="Click Me", command=clicked)
b.pack()

L = Label(root, text="ยังไม่มีออเดอร์")
L.config(font=("Courier", 44))
L.pack()

root.mainloop()
