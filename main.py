import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Form")
window.geometry('360x400')
window.configure(bg="#333333")

# Store correct credentials
correct_username = "modther"
correct_password = "12345"

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Function to perform login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == correct_username and password == correct_password:
        if remember_me_var.get():
            with open("remember.txt", "w") as f:
                f.write(username)
        else:
            open("remember.txt", "w").close()  # Clear file
        messagebox.showinfo(title="Login Success", message="You successfully logged in!")
    else:
        messagebox.showerror(title="Invalid Login", message="Username or password is incorrect.")

# Frame setup
frame = tkinter.Frame(bg="#333333")

login_label = tkinter.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))

password_label = tkinter.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

# 👁️ Show password checkbox
show_password_var = tkinter.BooleanVar()
show_password_check = tkinter.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password, bg="#333333", fg="#FFFFFF", activebackground="#333333", activeforeground="#FFFFFF", font=("Arial", 10))

# 🧠 Remember Me checkbox
remember_me_var = tkinter.BooleanVar()
remember_me_check = tkinter.Checkbutton(frame, text="Remember Me", variable=remember_me_var, bg="#333333", fg="#FFFFFF", activebackground="#333333", activeforeground="#FFFFFF", font=("Arial", 10))

# 🟩 Login button
login_button = tkinter.Button(frame, text="Login", bg="#817272", fg="#FFFFFF", font=("Arial", 16), command=login)

# Grid layout
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_label.grid(row=1, column=0, padx=10, sticky="w")
username_entry.grid(row=1, column=1, pady=10, padx=10)
password_label.grid(row=2, column=0, padx=10, sticky="w")
password_entry.grid(row=2, column=1, pady=10, padx=10)
show_password_check.grid(row=3, column=1, sticky="w")
remember_me_check.grid(row=4, column=1, sticky="w")
login_button.grid(row=5, column=0, columnspan=2, pady=20)

frame.pack()

# 🔄 Load remembered username if exists
try:
    with open("remember.txt", "r") as f:
        saved_username = f.read().strip()
        if saved_username:
            username_entry.insert(0, saved_username)
            remember_me_var.set(True)
except FileNotFoundError:
    pass

window.mainloop()

