import tkinter as tk

# Creates a basic graphical window
root = tk.Tk()
root.title("My First GUI")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
# Uncomment the line below to run the GUI loop in a local environment
# root.mainloop()