from tkinter import *
import tkinter.font as font
from basic_calculations import check_action
import logging

logging.basicConfig(level=logging.INFO)

root = Tk()
root.title("Basic Calculator")
btnFont = font.Font(family="Helvetica", size=15)
displeyFont = font.Font(family="Roman", size=20)

text_label = Label(root)
text_box = Entry(root, width=20, font=displeyFont, borderwidth=10)

text_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
text_box.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

num_A = None
num_B = None
action = None

def button_click(char):
    current = text_box.get()
    text_box.delete(0,END)
    if current == "0":
        text_box.insert(0, str(char))
    else:
        text_box.insert(0, str(current) + str(char))

def clear_displey():
    global num_A, num_B, action
    num_A = None
    num_B = None
    action = None
    text_box.delete(0,END)
    text_label.config(text="")

def valid_num():
    pass

def action_click(char):
    global num_A, num_B, action
    if num_A == None:
        print("First action")
        num_A = text_box.get()
        action = char
        text_box.delete(0,END)
        text_label.config(text=f"{num_A} {char}")
    
def displey_result(num1, num2, action):
    global num_A, num_B
    if num_A == None and num_B == None:
        logging.info(f"Num A = {num_A}, Num_B = {num_B}")
        return
    if text_box.get() == "":
        logging.info(f"Text_box is empty")
        return
    logging.info("Displey result")
    result = check_action(num1, num2, action)
    text_label.config(text=f"{num1} {action} {num2} = ")
    text_box.delete(0,END)
    text_box.insert(0, str(result))
    
btn_c = Button(root, text='C', padx=24, pady=20, font=btnFont, command=lambda: clear_displey())
btn_add = Button(root, text='+', padx=25, pady=20, font=btnFont, command=lambda: action_click("+"))
btn_subtract = Button(root, text='-', padx=26, pady=20, font=btnFont, command=lambda: action_click("-"))
btn_element = Button(root, text='√', padx=25, pady=20, font=btnFont, command=lambda: action_click("√"))
btn_multiplication = Button(root, text='*', padx=25, pady=20, font=btnFont, command=lambda: action_click("*"))
btn_modulo = Button(root, text='%', padx=22, pady=20, font=btnFont, command=lambda: action_click("%"))
btn_division = Button(root, text='/', padx=27, pady=20, font=btnFont, command=lambda: action_click("/"))
btn_exponentiation = Button(root, text='**', padx=23, pady=20, font=btnFont, command=lambda: action_click("**"))
btn_dot = Button(root, text='.', padx=25, pady=20, font=btnFont, command=lambda: button_click("."))
btn_result = Button(root, text='=', padx=25, pady=20, font=btnFont, command=lambda: displey_result(num_A, text_box.get(), action))
btn_1 = Button(root, text='1', padx=25, pady=20, font=btnFont, command=lambda: button_click(1))
btn_2 = Button(root, text='2', padx=25, pady=20, font=btnFont, command=lambda: button_click(2))
btn_3 = Button(root, text='3', padx=25, pady=20, font=btnFont, command=lambda: button_click(3))
btn_4 = Button(root, text='4', padx=25, pady=20, font=btnFont, command=lambda: button_click(4))
btn_5 = Button(root, text='5', padx=25, pady=20, font=btnFont, command=lambda: button_click(5))
btn_6 = Button(root, text='6', padx=25, pady=20, font=btnFont, command=lambda: button_click(6))
btn_7 = Button(root, text='7', padx=25, pady=20, font=btnFont, command=lambda: button_click(7))
btn_8 = Button(root, text='8', padx=25, pady=20, font=btnFont, command=lambda: button_click(8))
btn_9 = Button(root, text='9', padx=25, pady=20, font=btnFont, command=lambda: button_click(9))
btn_0 = Button(root, text='0', padx=25, pady=20, font=btnFont, command=lambda: button_click(0))

# Grid
btn_c.grid(row=2, column=0, padx=2, pady=2)
btn_add.grid(row=2, column=1, padx=2, pady=2)
btn_subtract.grid(row=2, column=2, padx=2, pady=2)
btn_element.grid(row=2, column=3, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)
btn_dot.grid(row=3, column=3, padx=2, pady=2)

btn_4.grid(row=4, column=0, padx=2, pady=2)
btn_5.grid(row=4, column=1, padx=2, pady=2)
btn_6.grid(row=4, column=2, padx=2, pady=2)
btn_modulo.grid(row=4, column=3, padx=2, pady=2)

btn_7.grid(row=5, column=0, padx=2, pady=2)
btn_8.grid(row=5, column=1, padx=2, pady=2)
btn_9.grid(row=5, column=2, padx=2, pady=2)
btn_exponentiation.grid(row=5, column=3, padx=2, pady=2)

btn_multiplication.grid(row=6, column=0, padx=2, pady=2)
btn_0.grid(row=6, column=1, padx=2, pady=2)
btn_division.grid(row=6, column=2, padx=2, pady=2)
btn_result.grid(row=6, column=3, padx=2, pady=2)

root.mainloop()
