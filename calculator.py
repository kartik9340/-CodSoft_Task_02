import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.root.config(bg="dark orange")

        # Initialize variables
        self.num1 = 0
        self.num2 = 0

        # GUI layout
        self.label = tk.Label(root, text="~~~~~Calculator~~~~~", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.num1_label = tk.Label(root, text="Enter first number:", font=("Arial", 12))
        self.num1_label.grid(row=1, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(root, width=20, font=("Arial", 12))
        self.num1_entry.grid(row=1, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(root, text="Enter second number:", font=("Arial", 12))
        self.num2_label.grid(row=2, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(root, width=20, font=("Arial", 12))
        self.num2_entry.grid(row=2, column=1, padx=10, pady=10)

        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add", width=15, font=("Arial", 12), command=self.add)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.subtract_button = tk.Button(root, text="Subtract", width=15, font=("Arial", 12), command=self.subtract)
        self.subtract_button.grid(row=4, column=1, padx=10, pady=10)

        self.multiply_button = tk.Button(root, text="Multiply", width=15, font=("Arial", 12), command=self.multiply)
        self.multiply_button.grid(row=5, column=0, padx=10, pady=10)

        self.divide_button = tk.Button(root, text="Divide", width=15, font=("Arial", 12), command=self.divide)
        self.divide_button.grid(row=5, column=1, padx=10, pady=10)

        self.continue_button = tk.Button(root, text="Continue", width=15, font=("Arial", 12), command=self.continue_calculating)
        self.continue_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add(self):
        self.get_input()
        result = self.num1 + self.num2
        self.show_result(result)

    def subtract(self):
        self.get_input()
        result = self.num1 - self.num2
        self.show_result(result)

    def multiply(self):
        self.get_input()
        result = self.num1 * self.num2
        self.show_result(result)

    def divide(self):
        self.get_input()
        if self.num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = self.num1 / self.num2
            self.show_result(result)

    def get_input(self):
        try:
            self.num1 = float(self.num1_entry.get())
            self.num2 = float(self.num2_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return

    def show_result(self, result):
        self.result_label.config(text=f"Result: {result}")

    def continue_calculating(self):
        # Clear the input fields to continue calculation
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
