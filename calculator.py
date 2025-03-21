import math
import sqlite3
import csv
import speech_recognition as sr
import pyttsx3
from tkinter import Tk, Entry, Button, StringVar, Label, Frame

# Basic mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y

# Additional mathematical functions
def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def floor_division(x, y):
    return x // y

def sqrt(x):
    return math.sqrt(x)

def sin_func(x):
    return math.sin(math.radians(x))

def cos_func(x):
    return math.cos(math.radians(x))

def tan_func(x):
    return math.tan(math.radians(x))

def log_func(x):
    return math.log10(x)

def ln_func(x):
    return math.log(x)

def factorial(x):
    return math.factorial(int(x))

# Evaluate user input expression safely
def evaluate_expression(expression):
    try:
        return eval(expression, {"__builtins__": {}}, {
            "add": add, "subtract": subtract, "multiply": multiply, "divide": divide,
            "modulus": modulus, "exponentiate": exponentiate, "floor_division": floor_division,
            "sqrt": sqrt, "sin": sin_func, "cos": cos_func, "tan": tan_func,
            "log": log_func, "ln": ln_func, "factorial": factorial
        })
    except Exception as e:
        return f"Error: {str(e)}"

# Store calculation results in a SQLite database
def store_result(expression, result):
    conn = sqlite3.connect("calculator_history.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS history (expression TEXT, result TEXT)")
    cursor.execute("INSERT INTO history VALUES (?, ?)", (expression, str(result)))
    conn.commit()
    conn.close()

# Export calculation history to a CSV file
def export_to_csv():
    conn = sqlite3.connect("calculator_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    with open("calculator_history.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Expression", "Result"])
        writer.writerows(cursor.fetchall())
    conn.close()

# GUI-based scientific calculator using Tkinter
def calculator_gui():
    def button_click(value):
        entry_var.set(entry_var.get() + str(value))

    def clear():
        entry_var.set("")

    def calculate():
        expression = entry_var.get()
        result = evaluate_expression(expression)
        store_result(expression, result)
        entry_var.set(result)
        speak_result(result)
    
    root = Tk()
    root.title("Scientific Calculator")
    root.geometry("400x600")

    entry_var = StringVar()
    entry = Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify='right')
    entry.pack(fill='both', padx=10, pady=10)
    
    button_frame = Frame(root)
    button_frame.pack()
    
    buttons = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '=', '+'),
        ('sin', 'cos', 'tan', 'sqrt'),
        ('log', 'ln', '!', 'C')
    ]
    
    for row_values in buttons:
        row_frame = Frame(button_frame)
        row_frame.pack()
        for value in row_values:
            Button(row_frame, text=value, font=("Arial", 15), width=5, height=2, command=lambda v=value: button_click(v) if v not in ('=', 'C') else (calculate() if v == '=' else clear())).pack(side='left', padx=5, pady=5)
    
    Button(root, text="Export History to CSV", font=("Arial", 12), command=export_to_csv).pack(pady=10)
    root.mainloop()

# Convert text results into speech
def speak_result(result):
    engine = pyttsx3.init()
    engine.say(f"The result is {result}")
    engine.runAndWait()

# Run the calculator GUI when the script is executed
if __name__ == "__main__":
    calculator_gui()
