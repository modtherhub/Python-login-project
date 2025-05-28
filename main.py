import tkinter

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x340')
window.configure(bg="#333333")

frame = tkinter.Frame(bg="#333333")

login_label = tkinter.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16) )
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="#817272", fg="#FFFFFF", font=("Arial", 16))


login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady = 40)
username_label.grid(row=1, column=0, padx = 10)
username_entry.grid(row=1, column=1, pady = 10, padx = 10)
password_label.grid(row=2, column=0, padx = 10)
password_entry.grid(row=2, column=1, pady = 10, padx = 10)
login_button.grid(row=3, column=0, columnspan=2, pady = 20)

frame.pack()

window.mainloop()