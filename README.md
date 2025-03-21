# Scientific Calculator with History, CSV Export, and Text-to-Speech

This Python script implements a scientific calculator with a graphical user interface (GUI) using Tkinter. It supports basic arithmetic operations, as well as advanced mathematical functions like trigonometry, logarithms, square roots, and factorials. The script also includes features to store calculation history in a SQLite database, export the history to a CSV file, and speak the results using text-to-speech.

## Features

* **Basic Arithmetic Operations:** Addition, subtraction, multiplication, and division.
* **Advanced Mathematical Functions:** Modulus, exponentiation, floor division, square root, sine, cosine, tangent, logarithm (base 10 and natural), and factorial.
* **GUI Interface:** User-friendly interface built with Tkinter.
* **Calculation History:** Stores calculation expressions and results in a SQLite database (`calculator_history.db`).
* **CSV Export:** Exports the calculation history to a CSV file (`calculator_history.csv`).
* **Text-to-Speech:** Speaks the calculation results using the `pyttsx3` library.
* **Safe Expression Evaluation:** Uses `eval` with restricted built-ins to prevent security vulnerabilities.

## Prerequisites

* Python 3.x
* Libraries: `tkinter`, `sqlite3`, `csv`, `pyttsx3`
    * Install required libraries using pip: `pip install pyttsx3`

## How to Run

1.  **Save the Script:** Save the provided Python code as a `.py` file (e.g., `scientific_calculator.py`).
2.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command: `python scientific_calculator.py`
3.  **Use the GUI:**
    * Enter mathematical expressions using the buttons provided.
    * Click `=` to calculate the result.
    * Click `C` to clear the input.
    * Click "Export History to CSV" to export the calculation history.

## Code

```python
import math
import sqlite3
import csv
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
Database
The script uses a SQLite database named calculator_history.db to store calculation history.
The database contains a table named history with columns expression (TEXT) and result (TEXT).
CSV Export
The calculation history is exported to a CSV file named calculator_history.csv.
The CSV file contains columns "Expression" and "Result".
Improvements (Optional)
Voice Input: Implement voice input using speech_recognition.
Error Handling: Add more robust error handling for invalid input and database operations.
Memory Functions: Add memory functions (M+, M-, MR, MC).
More Functions: Add more scientific functions and constants.
GUI Enhancements: Improve the GUI layout and design.
History Display: Add a feature to display the calculation history in the GUI.
Clear History: Add a feature to clear the calculation history.
More robust input validation: Add more validation to catch other types of errors.
