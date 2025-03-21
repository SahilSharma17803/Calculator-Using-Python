# Scientific Calculator with History and Speech

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
* Libraries: `tkinter`, `sqlite3`, `csv`, `speech_recognition`, `pyttsx3`
    * Install required libraries using pip: `pip install pyttsx3`

## How to Run

1.  **Save the Script:** Save the provided Python code as a `.py` file (e.g., `scientific_calculator.py`).
2.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command: `python scientific_calculator.py`
3.  **Use the GUI:**
    * Enter mathematical expressions using the buttons provided.
    * Click `=` to calculate the result.
    * Click `C` to clear the input.
    * Click "Export History to CSV" to export the calculation history.

## Code Explanation

* **Mathematical Functions:** Implements basic and advanced mathematical functions.
* **`evaluate_expression(expression)`:** Evaluates mathematical expressions safely using `eval` with restricted built-ins.
* **`store_result(expression, result)`:** Stores calculation expressions and results in a SQLite database.
* **`export_to_csv()`:** Exports the calculation history to a CSV file.
* **`calculator_gui()`:** Creates the GUI using Tkinter, handles button clicks, and performs calculations.
* **`speak_result(result)`:** Converts the calculation result to speech using `pyttsx3`.
* **`if __name__ == "__main__":`:** Runs the calculator GUI when the script is executed.

## Database

* The script uses a SQLite database named `calculator_history.db` to store calculation history.
* The database contains a table named `history` with columns `expression` (TEXT) and `result` (TEXT).

## CSV Export

* The calculation history is exported to a CSV file named `calculator_history.csv`.
* The CSV file contains columns "Expression" and "Result".

## Improvements (Optional)

* **Voice Input:** Implement voice input using `speech_recognition`.
* **Error Handling:** Add more robust error handling for invalid input and database operations.
* **Memory Functions:** Add memory functions (M+, M-, MR, MC).
* **More Functions:** Add more scientific functions and constants.
* **GUI Enhancements:** Improve the GUI layout and design.
* **History Display:** Add a feature to display the calculation history in the GUI.
* **Clear History:** Add a feature to clear the calculation history.
* **More robust input validation:** Add more validation to catch other types of errors.
