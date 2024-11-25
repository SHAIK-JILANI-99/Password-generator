import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")
        
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_numbers = numbers_var.get()
        use_specials = specials_var.get()
        include_name = name_var.get()
        
        char_pool = ""
        if use_uppercase:
            char_pool += string.ascii_uppercase
        if use_lowercase:
            char_pool += string.ascii_lowercase
        if use_numbers:
            char_pool += string.digits
        if use_specials:
            char_pool += string.punctuation
        
        name_input = name_entry.get()
        if include_name and name_input:
            char_pool += name_input
        
        if not char_pool:
            raise ValueError("At least one character set must be selected.")
        
        password = ''.join(random.choices(char_pool, k=length))
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Secure Password Generator")
root.configure(bg="#20232a")  # Neutral dark gray background

window_width = 520
window_height = 620
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.resizable(False, False)

title_label = tk.Label(
    root, 
    text="🔒 Secure Password Generator", 
    font=("Verdana", 18, "bold"), 
    bg="#20232a", 
    fg="#61dafb"
)
title_label.pack(pady=20)

separator = tk.Frame(root, height=2, width=450, bg="#61dafb")
separator.pack(pady=10)

content_frame = tk.Frame(root, bg="#282c34", bd=5, relief=tk.RIDGE)
content_frame.pack(pady=20, padx=20)

tk.Label(content_frame, text="Password Length:", font=("Verdana", 12), bg="#282c34", fg="#ffffff").grid(row=0, column=0, sticky="w", pady=10, padx=5)
length_entry = tk.Entry(content_frame, font=("Verdana", 12), bg="#3c4047", fg="white", insertbackground="white", width=15)
length_entry.grid(row=0, column=1, pady=10, padx=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)
name_var = tk.BooleanVar(value=False)

tk.Checkbutton(content_frame, text="Include Uppercase Letters", variable=uppercase_var, font=("Verdana", 10), bg="#282c34", fg="#ffffff", activebackground="#282c34", activeforeground="#ffffff", selectcolor="black").grid(row=1, column=0, columnspan=2, sticky="w", padx=5)
tk.Checkbutton(content_frame, text="Include Lowercase Letters", variable=lowercase_var, font=("Verdana", 10), bg="#282c34", fg="#ffffff", activebackground="#282c34", activeforeground="#ffffff", selectcolor="black").grid(row=2, column=0, columnspan=2, sticky="w", padx=5)
tk.Checkbutton(content_frame, text="Include Numbers", variable=numbers_var, font=("Verdana", 10), bg="#282c34", fg="#ffffff", activebackground="#282c34", activeforeground="#ffffff", selectcolor="black").grid(row=3, column=0, columnspan=2, sticky="w", padx=5)
tk.Checkbutton(content_frame, text="Include Special Characters", variable=specials_var, font=("Verdana", 10), bg="#282c34", fg="#ffffff", activebackground="#282c34", activeforeground="#ffffff", selectcolor="black").grid(row=4, column=0, columnspan=2, sticky="w", padx=5)

tk.Label(content_frame, text="Your Name (Optional):", font=("Verdana", 12), bg="#282c34", fg="#ffffff").grid(row=5, column=0, sticky="w", pady=10, padx=5)
name_entry = tk.Entry(content_frame, font=("Verdana", 12), bg="#3c4047", fg="white", insertbackground="white", width=15)
name_entry.grid(row=5, column=1, pady=10, padx=5)

tk.Checkbutton(content_frame, text="Include My Name in the Password", variable=name_var, font=("Verdana", 10), bg="#282c34", fg="#ffffff", activebackground="#282c34", activeforeground="#ffffff", selectcolor="black").grid(row=6, column=0, columnspan=2, sticky="w", padx=5)

generate_button = tk.Button(
    root, 
    text="Generate Password", 
    command=generate_password, 
    font=("Verdana", 12, "bold"), 
    bg="#e74c3c",  
    fg="white",  
    activebackground="#c0392b",  
    activeforeground="white", 
    width=20,
    bd=3,
    relief=tk.GROOVE
)
generate_button.pack(pady=20)

result_label = tk.Label(
    root, 
    text="", 
    font=("Verdana", 12, "italic"), 
    bg="#20232a", 
    fg="#1abc9c", 
    wraplength=450, 
    justify="center"
)
result_label.pack(pady=20)

footer = tk.Label(
    root, 
    text="Create strong passwords and secure your digital life!", 
    font=("Verdana", 10), 
    bg="#20232a", 
    fg="#61dafb"
)
footer.pack(side="bottom", pady=10)

tk.Label(root, text="💻", font=("Verdana", 20), bg="#20232a", fg="#61dafb").place(x=10, y=10)
tk.Label(root, text="🔐", font=("Verdana", 20), bg="#20232a", fg="#61dafb").place(x=470, y=10)
tk.Label(root, text="⚙", font=("Verdana", 20), bg="#20232a", fg="#61dafb").place(x=10, y=570)
tk.Label(root, text="🔑", font=("Verdana", 20), bg="#20232a", fg="#61dafb").place(x=470, y=570)

root.mainloop()