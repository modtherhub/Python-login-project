import tkinter

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x340')

login_label = tkinter.Label(window, text="Login")
username_label = tkinter.Label(window, text="Username")
username_entry = tkinter.Entry(window,)
password_label = tkinter.Label(window, text="Password")
login_label = tkinter.Entry(window, show="*")
login_button = tkinter.Button(window, text="Login")


login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0, )
username_entry.grid(row=1, column=1, )
password_label.grid(row=2, column=0, )
login_label.grid(row=2, column=1, )
login_button.grid(row=3, column=0, columnspan=2)

window.mainloop()