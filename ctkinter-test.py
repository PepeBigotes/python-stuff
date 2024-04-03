#!/usr/bin/env python3
#Created by PepeBigotes

from customtkinter import *


# MAIN WINDOW
root = CTk()
root.title("Testing CTkinter")
root.geometry("600x600")



# ACTIONS
def btn_func():
    string = "the botton was pressed"
    #print(string)
    framelabel.configure(text=string)

def slider_func(x: float):
    string = f"moved slider to {x}"
    #print(string)
    framelabel.configure(text=string)

switch_val = False
def switch_func():
    global switch_val
    switch_val = not switch_val
    string = f"switch {'on' if switch_val else 'off'}"
    #print(string)
    framelabel.configure(text=string)



# WIDGETS
label = CTkLabel(root, text='hello world')
label.pack(pady=20)

button = CTkButton(root,
    text='button',
    command=btn_func)
button.pack(pady=20)

frame = CTkFrame(root)
frame.pack()

framelabel = CTkLabel(frame, text="This text will change if you click stuff")
framelabel.pack()

slider = CTkSlider(root, command=slider_func)
slider.pack(padx=10, pady=10)

switch = CTkSwitch(root, command=switch_func)
switch.pack()



# MAINLOOP
root.mainloop()