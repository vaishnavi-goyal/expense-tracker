from tkinter import *
from tkinter import messagebox
import csv
import os

# Main Window
root = Tk()
root.title("Expense Tracker")
root.geometry("400x500")

balance = 0

# Functions
def add_expense():
    global balance

    category = category_entry.get()
    amount = amount_entry.get()

    if category == "" or amount == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    balance -= amount

    # Show in listbox
    expense_list.insert(END, f"{category} - ₹{amount}")

    # Update balance label
    balance_label.config(text=f"Balance: ₹{balance}")

    # Save to CSV
    file_exists = os.path.isfile("expenses.csv")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Category", "Amount"])

        writer.writerow([category, amount])

    # Clear entries
    category_entry.delete(0, END)
    amount_entry.delete(0, END)

    messagebox.showinfo("Success", "Expense Added")


# Heading
title = Label(root, text="Expense Tracker", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Category
Label(root, text="Category").pack()
category_entry = Entry(root, width=30)
category_entry.pack(pady=5)

# Amount
Label(root, text="Amount").pack()
amount_entry = Entry(root, width=30)
amount_entry.pack(pady=5)

# Add Button
add_btn = Button(root, text="Add Expense", command=add_expense)
add_btn.pack(pady=10)

# Balance Label
balance_label = Label(root, text="Balance: ₹0", font=("Arial", 14))
balance_label.pack(pady=10)

# Expense List
expense_list = Listbox(root, width=40, height=15)
expense_list.pack(pady=10)

# Run App
root.mainloop()
