from cProfile import label
from tkinter import *

root=Tk()
root.title("My GUI")
#กำหนดหน้าจอและตำแหน่ง
root.geometry("600x400")


#ใส่ข้อความบนหน้าจอ
myLabel1 = Label(root,text="Hello world",fg="orange",font=30).pack()
myLabel1 = Label(root,text="Hello world",fg="orange",font=30).pack()
#fungtion from button action
def showMessage():
    message=txt.get()
    print(message)
    Label(root,text=message,fg="white",font=30,bg="blue").pack()
    #Label(myWindow,text="Hello world",fg="red",bg="black",font=30).pack()
def openWindow():
    #หน้าจอที่สอง
    myWindow =Tk()
    myWindow.title("The second page")
    myWindow.geometry("600x400")

#message box
txt=StringVar()
myText=Entry(root,textvariable=txt).pack()
#button
btn1 = Button(root,text="登録",fg="white",bg="blue",command=showMessage).pack()
btn2 = Button(root,text="Open the second page",fg="white",bg="blue",command=openWindow).pack()

#รันดูผลลัพธ์หลังจากกำหนดคุณสมบัติเรียบร้อยแล้ว
root.mainloop() 


