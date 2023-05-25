from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

#Function with clock's format
def time():
    string = strftime('%H:%M:%S %p')            # Will display Hour, Minute, Seconds and AM or PM
    label.config(text=string)
    label.after(1000, time)

#This will change clock's color when you double tap on it
def change_color(event):
    colors = ["Cyan", "Magenta", "Yellow", "Green", "Red", "Blue"]         #<- We can add more colors :)
    current_color = label['foreground']
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    label.config(foreground=next_color)

#Clock with custom modification using tkinter
label = Label(root, font=("ds-digital", 80), background="black", foreground="Cyan")
label.pack(anchor="center")
label.bind("<Button-1>", change_color)

#This for calling function
time()
mainloop()
