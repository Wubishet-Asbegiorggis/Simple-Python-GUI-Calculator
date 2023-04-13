import math
from tkinter import *
from functools import partial
def funsm(lblsm, n1, n2):
    num1=(n1.get())
    num2=(n2.get())
    ressm=float (num1) + float (num2)
    lblsm.config(text=" The sum is : %f" % ressm, fg="blue", bg="white")
def fundf(lbldf, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    resdf = float (num1) - float (num2)
    lbldf.config(text=" The difference is : %f" % resdf,fg="blue",bg="white")
def funpr(lblpr, n1, n2):
        num1 = (n1.get())
        num2 = (n2.get())
        respr = float (num1) * float (num2)
        lblpr.config(text=" The product is : %f" % respr,fg="blue",bg="white")
def funqt(lbldv, n1, n2):
        num1 = (n1.get())
        num2 = (n2.get())
        resdv = float (num1) / float (num2)
        lbldv.config(text=" The quotient is : %f" % resdv, fg="blue", bg="white")
def funrem(remvar, n1, n2):
    num1=(n1.get())
    num2=(n2.get())
    resrem=float (num1) % float (num2)
    remvar.config(text="The remainder is : %f"%resrem,fg="blue",bg="white")
calo=Tk()
calo.geometry("500x500")
calo.title("       SIMPLE CALCULATOR WITH PYTHON TKINTER : ~")
number1=StringVar()
number2=StringVar()
labelNum1=Label(calo,text="Enter the first number ",fg='black',bg="white").place(x=10,y=50)
labelNum2=Label(calo,text="Enter the second number",fg="black",bg="white").place(x=10,y=90)
resultPosition=Label(calo)
resultPosition.place(x=80,y=180)
entryNum1=Entry(calo,textvariable=number1).place(x=150,y=50)
entryNum2=Entry(calo,textvariable=number2).place(x=150,y=90)
probsm=partial(funsm,resultPosition,number1,number2)
probdf=partial(fundf,resultPosition,number1,number2)
probpr=partial(funpr,resultPosition,number1,number2)
probdv=partial(funqt,resultPosition,number1,number2)
probrem=partial(funrem,resultPosition,number1,number2)
btnCal=Label(calo,text="Choose Operator",fg="green",bg="white").place(x=10,y=130)
btnSum=Button(calo,text="+",fg="blue",bg="white",command=probsm).place(x=120,y=130)
btnDiff=Button(calo,text="-",fg="blue",bg="white",command=probdf).place(x=150,y=130)
btnProd=Button(calo,text="x",fg="blue",bg="white",command=probpr).place(x=180,y=130)
btnDiv=Button(calo,text="/",fg="blue",bg="white",command=probdv).place(x=210,y=130)
btnrem=Button(calo,text="%",fg="blue",bg="white",command=probrem).place(x=240,y=130)
calo.mainloop()