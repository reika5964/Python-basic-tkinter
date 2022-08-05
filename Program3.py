from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color=askcolor()
    Mylabel=Label(text="color",bg=color[1]).pack()

def selectFile():
    fileopen=askopenfilename()
    fileContent =open(fileopen,encoding="utf8")
    mylabel =Label(text=fileContent.read()).pack()

btn =Button(text="カラーを選ぶ",command=selectColor).pack()
btn2 =Button(text="ファイルを選ぶ",command=selectFile).pack()
root.mainloop()