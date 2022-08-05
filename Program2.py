from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("My GUI")
root.geometry("500x500")
#สร้างเมนูที่หน้าหลัก
myMenu = Menu()
root.config(menu=myMenu)

#สร้างหน้าต่างใหม่
def showWindow():
    window =Tk()
    window.title("new window")
    window.mainloop()

def showProgram():
    messagebox.showinfo("このプログラムの情報;","開発者は井川礼香です。")  

def exitProgram(): 
    confirm =messagebox.askquestion("確認","閉じてもよろしいでしょうか？")
    if confirm == "yes":
        root.destroy()

#เพิ่มเมนุย่อย
menuItem= Menu()
menuItem.add_command(label="New Window",command=showWindow)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About",command=showProgram)
menuItem.add_command(label="Exit",command=exitProgram)

#เพิ่มเมนุหลัก
myMenu.add_cascade(label="file",menu=menuItem)
myMenu.add_cascade(label="edit")
myMenu.add_cascade(label="view")


root.mainloop()