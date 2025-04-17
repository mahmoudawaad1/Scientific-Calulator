import tkinter as tk
from tkinter import messagebox
import math
from fractions import Fraction

current_input = ""
history = []
history_index = -1

def append_to_input(value):
    global current_input
    if value == ".":
        if current_input and current_input[-1].isdigit():
            if '.' not in current_input.split('(')[-1]:
                current_input += value
        elif not current_input:
            current_input = "0."
    else:
        if value in "+-*/" and (current_input and current_input[-1] in "+-*/"):
            return
        elif current_input and current_input[-1] == ')' and value == '(':
            current_input += '*' + value
        elif value.isdigit():
            if current_input and (current_input[-1].isdigit() or current_input[-1] == ')'):
                current_input += value
            else:
                current_input += value
        elif value == ')':
            if current_input and (current_input[-1].isdigit() or current_input[-1] == ')'):
                current_input += value
            else:
                current_input += value
        elif value == '(':
            current_input += value
        else:
            if current_input and (current_input[-1].isdigit() or current_input[-1] == ')'):
                current_input += value
            else:
                current_input += value
    label_display.config(text=current_input)

def clear_input():
    global current_input
    current_input = ""
    label_display.config(text=current_input)

def clear_all_input():
    global current_input, history, history_index
    current_input = ""
    history = []
    history_index = -1
    label_display.config(text="")

def calculate_result():
    global current_input, history, history_index
    try:
        current_input = current_input.replace("^", "**")
        if '/' in current_input:
            current_input = str(Fraction(current_input))
        current_input = current_input.replace('%', '/100')
        result = eval(current_input)
        history.append((current_input, result))
        history_index = len(history)
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")
        current_input = ""
        label_display.config(text="")

def delete_last_char():
    global current_input
    current_input = current_input[:-1]
    label_display.config(text=current_input)

def square_root():
    global current_input
    try:
        value = float(current_input)
        result = math.sqrt(value)
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for square root.")

def factorial():
    global current_input
    try:
        value = int(current_input)
        if value < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = math.factorial(value)
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for factorial.")

def pi_value():
    global current_input
    current_input += str(math.pi)
    label_display.config(text=current_input)

def sin_value():
    global current_input
    try:
        value = float(current_input)
        result = math.sin(math.radians(value))
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for sine.")

def cos_value():
    global current_input
    try:
        value = float(current_input)
        result = math.cos(math.radians(value))
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for cosine.")

def tan_value():
    global current_input
    try:
        value = float(current_input)
        result = math.tan(math.radians(value))
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for tangent.")

def sinh_value():
    global current_input
    try:
        value = float(current_input)
        result = math.sinh(value)
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for sinh.")

def cosh_value():
    global current_input
    try:
        value = float(current_input)
        result = math.cosh(value)
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for cosh.")

def tanh_value():
    global current_input
    try:
        value = float(current_input)
        result = math.tanh(value)
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for tanh.")

def percentage():
    global current_input
    try:
        value = float(current_input)
        result = value / 100
        label_display.config(text=f"Result: {result}")
        current_input = str(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number to calculate percentage.")

def show_previous():
    global history, history_index
    if history_index > 0:
        history_index -= 1
        calculation, result = history[history_index]
        label_display.config(text=f"Prev: {calculation} = {result}")
    else:
        messagebox.showinfo("Info", "No previous calculation.")

def show_next():
    global history, history_index
    if history_index < len(history) - 1:
        history_index += 1
        calculation, result = history[history_index]
        label_display.config(text=f"Next: {calculation} = {result}")
    else:
        messagebox.showinfo("Info", "No next calculation.")

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg='#2c3e50')

label_display = tk.Label(root, text="", height=2, width=25, anchor="e", 
                        font=("Helvetica", 24), bg='#34495e', fg='#ecf0f1',
                        relief='ridge', borderwidth=3)
label_display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='nsew')

button_style = {
    'font': ("Helvetica", 16),
    'width': 5,
    'height': 2,
    'borderwidth': 2,
    'relief': 'raised'
}

buttons = [
    ('sin', 1, 0, {'bg': '#3498db', 'fg': 'white'}, sin_value),
    ('cos', 1, 1, {'bg': '#3498db', 'fg': 'white'}, cos_value),
    ('tan', 1, 2, {'bg': '#3498db', 'fg': 'white'}, tan_value),
    ('^', 1, 3, {'bg': '#3498db', 'fg': 'white'}, lambda: append_to_input("^")),
    ('√', 1, 4, {'bg': '#3498db', 'fg': 'white'}, square_root),
    ('π', 1, 5, {'bg': '#3498db', 'fg': 'white'}, pi_value),
    
    ('sinh', 2, 0, {'bg': '#3498db', 'fg': 'white'}, sinh_value),
    ('cosh', 2, 1, {'bg': '#3498db', 'fg': 'white'}, cosh_value),
    ('tanh', 2, 2, {'bg': '#3498db', 'fg': 'white'}, tanh_value),
    ('(', 2, 3, {'bg': '#7f8c8d', 'fg': 'white'}, lambda: append_to_input("(")),
    (')', 2, 4, {'bg': '#7f8c8d', 'fg': 'white'}, lambda: append_to_input(")")),
    ('!', 2, 5, {'bg': '#3498db', 'fg': 'white'}, factorial),
    
    ('7', 3, 0, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("7")),
    ('8', 3, 1, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("8")),
    ('9', 3, 2, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("9")),
    ('DEL', 3, 3, {'bg': '#e74c3c', 'fg': 'white'}, delete_last_char),
    ('AC', 3, 4, {'bg': '#e74c3c', 'fg': 'white'}, clear_all_input),
    ('C', 3, 5, {'bg': '#e74c3c', 'fg': 'white'}, clear_input),
    
    ('4', 4, 0, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("4")),
    ('5', 4, 1, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("5")),
    ('6', 4, 2, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("6")),
    ('*', 4, 3, {'bg': '#f39c12', 'fg': 'white'}, lambda: append_to_input("*")),
    ('/', 4, 4, {'bg': '#f39c12', 'fg': 'white'}, lambda: append_to_input("/")),
    ('%', 4, 5, {'bg': '#f39c12', 'fg': 'white'}, percentage),
    
    ('1', 5, 0, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("1")),
    ('2', 5, 1, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("2")),
    ('3', 5, 2, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("3")),
    ('+', 5, 3, {'bg': '#f39c12', 'fg': 'white'}, lambda: append_to_input("+")),
    ('-', 5, 4, {'bg': '#f39c12', 'fg': 'white'}, lambda: append_to_input("-")),
    ('=', 5, 5, {'bg': '#9b59b6', 'fg': 'white'}, calculate_result),
    
    ('0', 6, 0, {'bg': '#2ecc71', 'fg': 'white'}, lambda: append_to_input("0")),
    ('.', 6, 1, {'bg': '#7f8c8d', 'fg': 'white'}, lambda: append_to_input(".")),
    ('Prev', 6, 2, {'bg': '#95a5a6', 'fg': 'white'}, show_previous),
    ('Next', 6, 3, {'bg': '#95a5a6', 'fg': 'white'}, show_next)
]

for (text, row, col, style, command) in buttons:
    btn = tk.Button(root, text=text, **button_style, **style, command=command)
    btn.grid(row=row, column=col, padx=3, pady=3, sticky='nsew')

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(6):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
