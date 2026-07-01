import tkinter as tk

#display text

def display(value):
   entry.insert(tk.END,value)     

#calculate
def calculate():
    try :
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

#clear

def clear():
    entry.delete(0,tk.END)




window = tk.Tk()
#Title
window.title("SImple calculator")


entry  = tk.Entry(window)

label = tk.Label(window,text="your answer here :")


button1 = tk.Button(window,text=1,font=("Arial", 20),command=lambda:display("1"))
button2 = tk.Button(window,text=2,font=("Arial", 20),command=lambda:display("2"))
button3 = tk.Button(window,text=3,font=("Arial", 20), command=lambda: display("3"))
button4 = tk.Button(window,text=4,font=("Arial", 20), command=lambda: display("4"))
button5 = tk.Button(window,text=5,font=("Arial", 20), command=lambda: display("5"))
button6 = tk.Button(window,text=6,font=("Arial", 20), command=lambda: display("6"))
button7 = tk.Button(window,text=7,font=("Arial", 20), command=lambda: display("7"))
button8 = tk.Button(window,text=8,font=("Arial", 20), command=lambda: display("8"))
button9 = tk.Button(window,text=9,font=("Arial", 20), command=lambda: display("9"))
button0 = tk.Button(window,text=0,font=("Arial", 20), command=lambda: display("0"))

button_add = tk.Button(window,text="+",font=("Arial", 20), command=lambda: display("+"))
button_sub = tk.Button(window,text="-",font=("Arial", 20), command=lambda: display("-"))
button_mul = tk.Button(window,text="*",font=("Arial", 20), command=lambda: display("*"))
button_div = tk.Button(window,text="/",font=("Arial", 20), command=lambda: display("/"))

button_equals = tk.Button(window,text="=",font=("Arial", 20), command=calculate)
button_clear = tk.Button(window,text="C",font=("Arial", 20), command=clear)


#LAYOUT 

entry.grid(row=0, column=0, columnspan=4)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=2)
button_equals.grid(row=4,column=3)



window.mainloop()