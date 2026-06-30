import tkinter as tk

n = 0 
#defining a function
def count() :
    global n 
    n += 1
    label.config(text=n)


#window intialization
window = tk.Tk()

#window Title
window.title("click counter")

#widgets
label = tk.Label(window,text=0)
button = tk.Button(window,text="click me!!!",command= count)

#placing wingets
label.pack()
button.pack()

#window opening
window.mainloop()