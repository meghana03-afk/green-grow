import tkinter as tk

def add():
    r=int(num1.get())+int(num2.get())
    lr.config(text="result:"+str(r))

def sub():
    r=int(num1.get())-int(num2.get())
    lr.config(text="result:"+str(r))

def mul():
    r=int(num1.get())*int(num2.get())
    lr.config(text="result:"+str(r))

def div():
    r=int(num1.get())/int(num2.get())
    lr.config(text="result:"+str(r))

w=tk.Tk()
w.title('calculator')
w.geometry('600x400')
l=tk.Label(w,text='simple calculator')


num1=tk.Entry(w)
num1.grid(row=1,column=0)

num2=tk.Entry(w)
num2.grid(row=1,column=2)

plus=tk.Label(w,text="+")
plus.grid(row=1,column=1)

b1=tk.Button(w,text='add',command=add)
b1.grid(row=2,column=0)

b2=tk.Button(w,text='sub',command=sub)
b2.grid(row=2,column=1)

b3=tk.Button(w,text='mul',command=mul)
b3.grid(row=2,column=2)

b4=tk.Button(w,text='div',command=div)
b4.grid(row=2,column=3)

lr=tk.Label(w,text="result:")
lr.grid(row=3,column=1)

           

w.mainloop()
