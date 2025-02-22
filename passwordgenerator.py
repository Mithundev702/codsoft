import tkinter as tk
from tkinter import messagebox
import random
import string


# Function to generate a random password
def generate_password():
    length = length_var.get()
    characters = ""
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character set!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# Initialize Tkinter root
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#1E73BE")  # Dark blue background

# Password Label
label = tk.Label(root, text="Password Generator", font=("Arial", 14, "bold"), bg="#1E73BE", fg="white")
label.pack(pady=10)

# Password Entry
password_var = tk.StringVar()
entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=24, justify="center", bd=2, relief="groove")
entry.pack(pady=5)

# Copy Button
copy_button = tk.Button(root, text="📋", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack()

# Password Length Slider
length_var = tk.IntVar(value=8)
slider_frame = tk.Frame(root, bg="#1E73BE")
slider_frame.pack(pady=10)
slider_label = tk.Label(slider_frame, text="Length:", font=("Arial", 10, "bold"), bg="#1E73BE", fg="white")
slider_label.pack(side="left")
slider = tk.Scale(slider_frame, from_=6, to=20, orient="horizontal", variable=length_var, font=("Arial", 10),
                  length=200, bg="#1E73BE", fg="white", highlightthickness=0)
slider.pack(side="right")

# Character Set Options
options_frame = tk.Frame(root, bg="#1E73BE")
options_frame.pack(pady=10)

lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

lowercase_button = tk.Checkbutton(options_frame, text="a-z", variable=lowercase_var, font=("Arial", 10, "bold"),
                                  bg="#D4A017", fg="black", indicatoron=False, width=5)
lowercase_button.grid(row=0, column=0, padx=5)
uppercase_button = tk.Checkbutton(options_frame, text="A-Z", variable=uppercase_var, font=("Arial", 10, "bold"),
                                  bg="white", fg="black", indicatoron=False, width=5)
uppercase_button.grid(row=0, column=1, padx=5)
digits_button = tk.Checkbutton(options_frame, text="0-9", variable=digits_var, font=("Arial", 10, "bold"), bg="white",
                               fg="black", indicatoron=False, width=5)
digits_button.grid(row=0, column=2, padx=5)
symbols_button = tk.Checkbutton(options_frame, text="!?", variable=symbols_var, font=("Arial", 10, "bold"), bg="white",
                                fg="black", indicatoron=False, width=5)
symbols_button.grid(row=0, column=3, padx=5)

# Generate Button
generate_button = tk.Button(root, text="GENERATE", command=generate_password, font=("Arial", 12, "bold"), bg="#004A99",
                            fg="white", padx=10, pady=5, relief="raised")
generate_button.pack(pady=10)

# Run the application
root.mainloop()
