import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        choice = operation_var.get()

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        else:
            result = "Invalid choice!"

        result_label.config(text=f"{num1} {get_operator(choice)} {num2} = {result}")
    except ValueError:
        result_label.config(text="Invalid input!")

def get_operator(choice):
    if choice == 1:
        return "+"
    elif choice == 2:
        return "-"
    elif choice == 3:
        return "*"
    elif choice == 4:
        return "/"

root = tk.Tk()
root.title("Basic Calculator")

operation_var = tk.IntVar()
operation_var.set(1)

num1_label = tk.Label(root, text="Number 1:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

num2_label = tk.Label(root, text="Number 2:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

operation_frame = tk.Frame(root)
operation_frame.pack()

add_radio = tk.Radiobutton(operation_frame, text="Addition", variable=operation_var, value=1)
add_radio.pack(side=tk.LEFT)
subtract_radio = tk.Radiobutton(operation_frame, text="Subtraction", variable=operation_var, value=2)
subtract_radio.pack(side=tk.LEFT)
multiply_radio = tk.Radiobutton(operation_frame, text="Multiplication", variable=operation_var, value=3)
multiply_radio.pack(side=tk.LEFT)
divide_radio = tk.Radiobutton(operation_frame, text="Division", variable=operation_var, value=4)
divide_radio.pack(side=tk.LEFT)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()