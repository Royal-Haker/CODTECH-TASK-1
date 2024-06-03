from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
            scrvalue.set(value)
            screen.update()
        except Exception as e:
            scrvalue.set("Error")
            screen.update()
    elif text == "C":
        scrvalue.set("")
        screen.update()
    else:
        scrvalue.set(scrvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("300x400")

root.minsize(300,450)

root.title("Calculator By Rehaan")
root.wm_iconbitmap("1.ico")

scrvalue = StringVar()
scrvalue.set("")
screen = Entry(root, textvariable=scrvalue, font="lucida 20 bold", bd=10, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, ipady=10, pady=10, padx=10)

# Creating the buttons
button_frame = Frame(root)
button_frame.pack()

buttons = [
    ('7', 'lightgrey'), ('8', 'lightgrey'), ('9', 'lightgrey'), ('/', 'orange'),
    ('4', 'lightgrey'), ('5', 'lightgrey'), ('6', 'lightgrey'), ('*', 'orange'),
    ('1', 'lightgrey'), ('2', 'lightgrey'), ('3', 'lightgrey'), ('-', 'orange'),
    ('C', 'red'), ('0', 'lightgrey'), ('=', 'green'), ('+', 'orange')
]

i = 0
for btn, color in buttons:
    button = Button(button_frame, text=btn, font="lucida 15 bold", padx=20, pady=20, bg=color)
    button.grid(row=i//4, column=i%4)
    button.bind("<Button-1>", click)
    i += 1

root.mainloop()
