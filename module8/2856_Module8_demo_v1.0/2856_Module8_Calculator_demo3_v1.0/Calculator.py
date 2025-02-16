import tkinter as tk

# Step 1: Create the main application window
root = tk.Tk()
root.title("Calculator")

# Step 2: Create a StringVar to store user input
entry_var = tk.StringVar()

# Step 3: Create an Entry widget for input display
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Step 4: Define calculator buttons
buttons = [
    ('9', '8', '7', '/'),
    ('6', '5', '4', '*'),
    ('3', '2', '1', '-'),
    ('⌫', '0', 'C', '+')
]

# Step 5: Create and place buttons in the grid
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 18), padx=15, pady=15)
        btn.grid(row=i+1, column=j, sticky='nsew')
        
        # Step 6: Assign functions to buttons
        if text == "=":
            btn.config(command=lambda: entry_var.set(eval(entry_var.get()) if entry_var.get() else ""))
        elif text == "C":
            btn.config(command=lambda: entry_var.set(""))
        elif text == "⌫":
            btn.config(command=lambda: entry_var.set(entry_var.get()[:-1]))
        else:
            btn.config(command=lambda t=text: entry_var.set(entry_var.get() + t))

# Step 7: Create and configure the Equal button
equal_btn = tk.Button(root, text="=", font=("Arial", 18), padx=15, pady=15)
equal_btn.grid(row=5, column=1, columnspan=2, sticky='nsew')
equal_btn.config(command=lambda: entry_var.set(eval(entry_var.get()) if entry_var.get() else ""))

# Step 8: Run the main event loop
root.mainloop()
