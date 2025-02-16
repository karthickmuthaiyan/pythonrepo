import tkinter as tk

# 1. Button

root = tk.Tk()
button = tk.Button(root, text="Click Me")
button.pack()
root.mainloop()


# 2. Label

root = tk.Tk()
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
root.mainloop()


# 3. Canvas

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=100, bg="lightblue")
canvas.pack()
root.mainloop()

# 4. ComboBox

from tkinter import ttk
root = tk.Tk()
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()
root.mainloop()

# 5. CheckButton

root = tk.Tk()
chk = tk.Checkbutton(root, text="Check me")
chk.pack()
root.mainloop()


# 6. RadioButton

root = tk.Tk()
rb = tk.Radiobutton(root, text="Option 1", value=1)
rb.pack()
root.mainloop()


# 7. Entry (Text Input)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
root.mainloop()


# 8. Frame

root = tk.Tk()
frame = tk.Frame(root, width=200, height=100, bg="gray")
frame.pack()
root.mainloop()

# 9. Message

root = tk.Tk()
msg = tk.Message(root, text="This is a message widget")
msg.pack()
root.mainloop()


# 10. Text (Multiline)

root = tk.Tk()
text = tk.Text(root, height=5, width=40)
text.pack()
root.mainloop()


# 11. Menu

def hello():
    print("Hello!")

root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
submenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Say Hello", command=hello)
root.mainloop()


# 12. Spinbox

root = tk.Tk()
spin = tk.Spinbox(root, from_=0, to=10)
spin.pack()
root.mainloop()


# 13. Scale (Slider)

root = tk.Tk()
scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack()
root.mainloop()


# 14. Scrollbar

root = tk.Tk()
text = tk.Text(root, height=5, width=40)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.pack(side="left")
scrollbar.pack(side="right", fill="y")
root.mainloop()


# Tkinter Geometry Management: Label Pack Example

root = tk.Tk()
label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="blue")
label1.pack(fill="both", expand=True)
label2.pack(fill="both", expand=True)
root.mainloop()


#-------------------------------------------------------------------#
#   Select the text and Press Ctrl + / to remove the indentations   #
#         Make sure to select and Indent the Upper Block            #
#-------------------------------------------------------------------#

#-------------------------------------------------#
#    Final Output with all the above components   #
#-------------------------------------------------#

#import tkinter as tk
# from tkinter import ttk, messagebox, colorchooser

# # Function for Button Click
# def button_click():
#     messagebox.showinfo("Action", "Button Clicked!")

# # Function for Color Picker
# def pick_color():
#     color = colorchooser.askcolor()[1]
#     if color:
#         color_label.config(bg=color, text=color)

# # Main Window
# root = tk.Tk()
# root.title("Complete Tkinter UI")
# root.geometry("600x600")

# # ------------------- Menu Bar -------------------
# menu_bar = tk.Menu(root)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)
# root.config(menu=menu_bar)

# # ------------------- Widgets -------------------

# # Labels
# tk.Label(root, text="Welcome to Tkinter UI", font=("Arial", 14, "bold")).pack(pady=5)

# # Buttons
# tk.Button(root, text="Click Me", command=button_click).pack(pady=5)

# # Entry Field
# entry = tk.Entry(root, width=30)
# entry.pack(pady=5)
# entry.insert(0, "Enter text here...")

# # Text Box
# text_box = tk.Text(root, height=3, width=40)
# text_box.pack(pady=5)
# text_box.insert("1.0", "This is a multi-line text box")

# # CheckButton
# chk_var = tk.IntVar()
# chk = tk.Checkbutton(root, text="Check Me", variable=chk_var)
# chk.pack(pady=5)

# # RadioButtons
# radio_var = tk.StringVar(value="Option 1")
# tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1").pack()
# tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2").pack()

# # ComboBox
# combo = ttk.Combobox(root, values=["Option A", "Option B", "Option C"])
# combo.pack(pady=5)
# combo.set("Select an option")

# # SpinBox
# spin = tk.Spinbox(root, from_=1, to=10)
# spin.pack(pady=5)

# # Scale (Slider)
# scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
# scale.pack(pady=5)

# # Scrollbar with Text
# scroll_text = tk.Text(root, height=5, width=40)
# scrollbar = tk.Scrollbar(root, command=scroll_text.yview)
# scroll_text.config(yscrollcommand=scrollbar.set)
# scroll_text.pack(side="left", padx=5, pady=5)
# scrollbar.pack(side="right", fill="y")

# # Canvas
# canvas = tk.Canvas(root, width=100, height=50, bg="lightblue")
# canvas.pack(pady=5)

# # Message
# msg = tk.Message(root, text="This is a message widget")
# msg.pack(pady=5)

# # Frame
# frame = tk.Frame(root, width=100, height=50, bg="gray")
# frame.pack(pady=5)

# # Color Picker
# color_button = tk.Button(root, text="Pick a Color", command=pick_color)
# color_button.pack(pady=5)
# color_label = tk.Label(root, text="Selected Color", bg="white", width=20)
# color_label.pack(pady=5)

# # Run the Tkinter event loop
# root.mainloop()
