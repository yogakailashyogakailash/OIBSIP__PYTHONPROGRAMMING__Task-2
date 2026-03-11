import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(w.get())
        height = float(h.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")


tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg)").pack()
w = tk.Entry(root)
w.pack()

tk.Label(root, text="Height (m)").pack()
h = tk.Entry(root)
h.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
