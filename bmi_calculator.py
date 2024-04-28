import tkinter as tk
from tkinter import messagebox

# Define a function to calculate BMI
def calculate_bmi(weight, height):
    #return weight / (height ** 2)
    height_meters = height / 100
    return weight / (height_meters ** 2)

# Define a function to classify BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Define a function to handle button click event
def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = calculate_bmi(weight, height)
        bmi_category = classify_bmi(bmi)
        result_text.set(f"Your BMI is: {bmi:.2f}\nYou are classified as: {bmi_category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

# Define a function to handle clear button click event
def clear_button_clicked():
    weight_entry.delete(0, tk.END)  # Clear weight entry
    height_entry.delete(0, tk.END)  # Clear height entry
    result_text.set("")  # Clear result label

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Change window background color and border width
root.configure(background="white", border=50)

# Create weight label and entry
weight_label = tk.Label(root, text="Weight (kg):", background="white")
weight_label.grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root, background="white")
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# Create height label and entry
height_label = tk.Label(root, text="Height (cm):", background="white")
height_label.grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_button_clicked, background="lightgray")
#calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
calculate_button.grid(row=2, column=0, padx=5, pady=5)


# Create clear button
clear_button = tk.Button(root, text="Clear", command=clear_button_clicked, background="lightgray")
#clear_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
clear_button.grid(row=2, column=1, padx=5, pady=5)

# Create result label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, background="white")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()