from tkinter import *

root = Tk()
root.title("Data Entry")
root.geometry("300x200")

Label(text="名前").grid(row=0)
Label(text="苗字").grid(row=1)
Label(text="電話番号").grid(row=2)

et1=Entry()
et1.grid(row=0,column=1)
et1.insert(0,"kong ")

et2=Entry()
et2.grid(row=1,column=1)
et2.insert(0,"kong ")

et3=Entry()
et3.grid(row=2,column=1)
et3.insert(0,"kong ")

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

button = Button(text="削除",command=deleteText).grid(row=3,column=1)

root.mainloop()