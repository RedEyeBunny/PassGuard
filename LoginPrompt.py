import tkinter as tk
from tkinter import messagebox
import PasswordManager
import PasswordEncode


class LoginPage(tk.Tk): # here instead of root we have self doing all the functions of 'root'.
    def __init__(self):
        super().__init__()
        self.title('Login Page')
        self.maxsize(200,200)
        self.minsize(200,200)
        self.LoginWidgetsGrouped()

    def LoginWidgetsGrouped(self):
        self.label_Information = tk.Label(self, text="Enter login password").place(x=30,y=20)
        self.Password_Entry = tk.Entry(self)
        self.Password_Entry.place(x=20,y=50)
        self.Login_Button = tk.Button(self, text='Login',command=self.OnLoginClick).pack(pady=90)

    def OnLoginClick(self):
        Password_Entry_Text = self.Password_Entry.get()
        if Password_Entry_Text == 'Harsh211b133':
            #self.withdraw()
            pm1 = PasswordManager.PasswordManager() # open the password manager

        else:# if password is wrong
            messagebox.showerror('Wrong Password', 'Wrong Password')
