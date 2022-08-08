
from locale import currency
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Data Entry")

#Input
money= IntVar()
Label(text="金額(THB)",padx=10,font=("MSゴシック", "14")).grid(row=0,sticky=W)
et1=Entry(font=("MSゴシック", "14"),width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="外貨を選択してください。")
Label(text="外貨",padx=10,font=("MSゴシック", "14")).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=("MSゴシック", "14"),textvariable=choice)
combo["values"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

#Output
Label(text="計算結果",padx=10,font=("MSゴシック", "14")).grid(row=2,sticky=W)
et2=Entry(font=("MSゴシック", "14"),width=30)
et2.grid(row=2,column=1)

def calculate():
    amount = money.get()
    currency= choice.get()

    if currency == "EUR":
        et2.delete(0,END)
        result=((amount*0.026),"EUR(ユーロ)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result=((amount*3.486),"JPY(円)")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result=((amount*0.031),"USD(ドル)")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result=((amount*0.023),"GBP(ポーン)")
        et2.insert(0,result)
    else    :
        et2.delete(0,END)
        result="計算出来ません。"
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
Button(text="計算",font=("MSゴシック", "10"),width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="リセット",font=("MSゴシック", "10"),width=15,command=deleteText).grid(row=3,column=1,sticky=E)

root.mainloop()