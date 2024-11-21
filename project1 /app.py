import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

# Functionality
def add_item():
    item = item_entry.get()
    try:
        price = float(price_entry.get())
        if item and price >= 0:
            items_listbox.insert(tk.END, f"{item}: ${price:.2f}")
            items.append((item, price))
            item_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid item name or price.")
    except ValueError:
        messagebox.showerror("Error", "Price must be a number.")

def calculate_total():
    total = sum(price for _, price in items)
    total_label.config(text=f"Total: ${total:.2f}")

def save_transaction():
    if not items:
        messagebox.showerror("Error", "No items to save.")
        return

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Transaction"
    )
    if filename:
        with open(filename, "w") as file:
            file.write(f"Transaction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("Items:\n")
            for item, price in items:
                file.write(f"{item}: ${price:.2f}\n")
            total = sum(price for _, price in items)
            file.write(f"\nTotal: ${total:.2f}")
        messagebox.showinfo("Saved", "Transaction saved successfully.")
        clear_all()

def clear_all():
    items_listbox.delete(0, tk.END)
    total_label.config(text="Total: $0.00")
    items.clear()

# GUI
root = tk.Tk()
root.title("Point of Sale")

items = []

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

tk.Label(input_frame, text="Item:").grid(row=0, column=0, padx=5, pady=5)
item_entry = tk.Entry(input_frame)
item_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Price:").grid(row=1, column=0, padx=5, pady=5)
price_entry = tk.Entry(input_frame)
price_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Item", command=add_item)
add_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

# Items Listbox
items_frame = tk.Frame(root, padx=10, pady=10)
items_frame.pack()

items_listbox = tk.Listbox(items_frame, width=40, height=10)
items_listbox.pack()

# Total and Buttons
total_frame = tk.Frame(root, padx=10, pady=10)
total_frame.pack()

total_label = tk.Label(total_frame, text="Total: $0.00", font=("Arial", 14))
total_label.pack(side=tk.LEFT, padx=10)

calculate_button = tk.Button(total_frame, text="Calculate Total", command=calculate_total)
calculate_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(total_frame, text="Save Transaction", command=save_transaction)
save_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(total_frame, text="Clear All", command=clear_all)
clear_button.pack(side=tk.LEFT, padx=10)

root.mainloop()