import tkinter as tk
from tkinter import messagebox

# Function to calculate the sum of two numbers
def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum_nums = num1 + num2
        messagebox.showinfo("Result", f"The sum of {num1} and {num2} is: {sum_nums}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to calculate the difference between two numbers
def calculate_diff():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        diff_nums = num1 - num2
        messagebox.showinfo("Result", f"The difference between {num1} and {num2} is: {diff_nums}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to calculate the product of two numbers
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        messagebox.showinfo("Result", f"The product of {num1} and {num2} is: {product}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to calculate the division of two numbers
def calculate_div():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        div_nums = num1 / num2
        messagebox.showinfo("Result", f"The division of {num1} by {num2} is: {div_nums}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to calculate the modulo (remainder) of two numbers
def calculate_modulo():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        mod_nums = num1 % num2
        messagebox.showinfo("Result", f"The remainder of {num1} divided by {num2} is: {mod_nums}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Number Operations")

# Set the size of the window (increase width and height)
root.geometry("500x400")  # Width: 500px, Height: 400px

# Title label
font_bold = ("Helvetica", 18, "bold")
label_title = tk.Label(root, text="Simple Math Operations Calculator", fg="white", bg="Dark Green",font=("Arial", 15))
label_title.grid(row=0, columnspan=3, padx=70, pady=30)

# Labels and entry boxes for the numbers
label1 = tk.Label(root, text="Enter first number:", font=("Arial", 10, "bold"))
label1.grid(row=1, column=0, padx=10, pady=10)  # Updated row and column
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter second number:", font=("Arial", 10, "bold"))
label2.grid(row=2, column=0, padx=10, pady=10)  # Updated row and column
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)

# Frame for arithmetic operation buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Arithmetic buttons
sum_button = tk.Button(button_frame, text="Sum", command=calculate_sum, font=("Helvetica", 10, "bold"))
sum_button.grid(row=0, column=0, padx=10, pady=10)

diff_button = tk.Button(button_frame, text="Difference", command=calculate_diff, font=("Helvetica", 10, "bold"))
diff_button.grid(row=0, column=1, padx=10, pady=10)

product_button = tk.Button(button_frame, text="Product", command=calculate_product, font=("Helvetica", 10, "bold"))
product_button.grid(row=0, column=2, padx=10, pady=10)

div_button = tk.Button(button_frame, text="Division", command=calculate_div, font=("Helvetica", 10, "bold"))
div_button.grid(row=1, column=0, padx=10, pady=10)

mod_button = tk.Button(button_frame, text="Modulo", command=calculate_modulo, font=("Helvetica", 10, "bold"))
mod_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
