import mysql.connector as sqltor
import tkinter as tk
from tkinter import messagebox
import random
import string
import ManagerOperations


class PasswordManager: # here there is no tk.Tk() because of the code 'self.root = tk.Tk()',
                       # the screen is already
                       # called there
    def __init__(self):
        super().__init__()
        self.db = sqltor.connect(
            host='localhost',
            user='frost-ASUS-Gaming',
            password='H@rsh#2003',
            database='sec'
        )
        self.cursor = self.db.cursor()
        self.root = tk.Tk()
        self.root.title("PassGuard")
        self.root.geometry("200x200")
        self.root.minsize(200, 300)
        self.root.maxsize(200, 300)
        self.ButtonPlacementandStart()  # place all the buttons at their intended place

    def AddWindow(self):
        addWindow = tk.Toplevel(self.root)
        addWindow.title("Add Details")
        addWindow.geometry('400x250')
        addWindow.minsize(400, 250)
        addWindow.maxsize(400, 250)
        tk.Label(addWindow, text="Website Name").place(x=20, y=20)
        website_name = tk.Entry(addWindow)
        website_name.place(x=150, y=20)
        tk.Label(addWindow, text="Website URL").place(x=20, y=50)
        website_url = tk.Entry(addWindow)
        website_url.place(x=150, y=50)
        tk.Label(addWindow, text="Login/Mail-Id").place(x=20, y=80)
        login = tk.Entry(addWindow)
        login.place(x=150, y=80)
        tk.Label(addWindow, text="Password").place(x=20, y=110)
        password = tk.Entry(addWindow)
        password.place(x=150, y=110)
        tk.Label(addWindow, text="Pin").place(x=20, y=140)
        pin = tk.Entry(addWindow)
        pin.place(x=150, y=140)
        tk.Label(addWindow, text="Email").place(x=20, y=170)
        email = tk.Entry(addWindow)
        email.place(x=150, y=170)

        def addPassword():
            value1 = website_name.get()
            value1_hashed = website_name.get().encode()
            value2 = website_url.get()
            value2_hashed = website_url.get().encode()
            value3 = login.get()
            value3_hashed = login.get().encode()
            value4 = password.get()
            value4_hashed = password.get().encode()
            value5 = pin.get()
            value5_hashed = pin.get().encode()
            value6 = email.get()
            value6_hashed = email.get().encode()
            if value1 == "" or value2 == "" or value3 == "" or value4 == "" or value5 == "" or value6 == "":
                messagebox.showwarning("!Warning!", "Fill All fields")
            else:
                query = f"INSERT INTO info VALUES ('{value1}', '{value2}', '{value3}', '{value4}', '{value5}', '{value6}')"
                self.cursor.execute(query)
                self.db.commit()
                messagebox.showinfo("Success", "Values updated")

        tk.Button(addWindow, text="Add", command=addPassword).place(x=200, y=210)

    def LookUpWindow(self):
        LookupWindow = tk.Toplevel(self.root)
        LookupWindow.title("LookUp Details")
        LookupWindow.geometry('200x200')
        LookupWindow.minsize(200, 200)
        LookupWindow.maxsize(200, 200)
        tk.Label(LookupWindow, text="Website Name").pack(pady=10)
        website_name = tk.Entry(LookupWindow)
        website_name.pack(pady=10)

        def LookUpResultWindow():
            site = website_name.get()
            if site == "":
                messagebox.showwarning("Error", "Enter a value")
            else:
                self.cursor.execute(f"select * from info where Information = '{site}'")
                res = self.cursor.fetchall()
                v1 = res[0][0]
                v2 = res[0][1]
                v3 = res[0][2]
                v4 = res[0][3]
                v5 = res[0][4]
                v6 = res[0][5]
                ResultWindow = tk.Toplevel(self.root)
                ResultWindow.title("LookUp Details")
                ResultWindow.geometry('400x250')
                ResultWindow.minsize(400, 250)
                ResultWindow.maxsize(400, 250)
                tk.Label(ResultWindow, text="Website Name").place(x=20, y=20)
                wn = tk.Text(ResultWindow, height=1, width=20)
                wn.place(x=150, y=20)
                wn.insert(tk.END, v1)
                tk.Label(ResultWindow, text="Website URL").place(x=20, y=50)
                wurl = tk.Text(ResultWindow, height=1, width=20)
                wurl.place(x=150, y=50)
                wurl.insert(tk.END, v2)
                tk.Label(ResultWindow, text="Login/Mail-Id").place(x=20, y=80)
                lmid = tk.Text(ResultWindow, height=1, width=20)
                lmid.place(x=150, y=80)
                lmid.insert(tk.END, v3)
                tk.Label(ResultWindow, text="Password").place(x=20, y=110)
                pw = tk.Text(ResultWindow, height=1, width=20)
                pw.place(x=150, y=110)
                pw.insert(tk.END, v4)
                tk.Label(ResultWindow, text="Pin").place(x=20, y=140)
                pi = tk.Text(ResultWindow, height=1, width=20)
                pi.place(x=150, y=140)
                pi.insert(tk.END, v5)
                tk.Label(ResultWindow, text="Email").place(x=20, y=170)
                em = tk.Text(ResultWindow, height=1, width=20)
                em.place(x=150, y=170)
                em.insert(tk.END, v6)

        tk.Button(LookupWindow, text="See Details", command=LookUpResultWindow).pack(pady=10)

    def ChangePasswordWindow(self):
        ChangePassWindow = tk.Toplevel(self.root)
        ChangePassWindow.title("Change Password Details")
        ChangePassWindow.geometry('200x200')
        ChangePassWindow.minsize(400, 200)
        ChangePassWindow.maxsize(400, 200)
        tk.Label(ChangePassWindow, text="Name of website").place(x=25, y=25)
        web_name=tk.Entry(ChangePassWindow).place(x=170,y=25)
        tk.Label(ChangePassWindow, text="Username/mail-id").place(x=25, y=60)
        user_name=tk.Entry(ChangePassWindow).place(x=170,y=60)
        tk.Label(ChangePassWindow, text='New Password').place(x=25, y=100)
        new_pass = tk.Entry(ChangePassWindow).place(x=170, y=100)


        def ChangePassword():
            query = f"UPDATE info SET Password ={new_pass} WHERE Information={web_name} and Login_name={user_name}"
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success", "Values updated")

        tk.Button(ChangePassWindow,text='Ok',command=ChangePassword).place(x=200,y=140)
    def random_password_generator(self):
        characters = string.ascii_letters + string.digits + string.punctuation.replace(' ', '')
        ManOps = ManagerOperations.ManagerOperations()
        password_length = random.randint(8, 12)
        password = ''.join(random.sample(characters, password_length))
        Password_window = tk.Toplevel(self.root)
        Password_window.title("Random Password")
        Password_window.geometry('200x200')
        Password_window.minsize(200, 200)
        Password_window.maxsize(200, 200)
        tk.Label(Password_window, text='Random password is ').pack(pady=30)
        Password = tk.Text(Password_window, height=1, width=20)
        Password.pack(pady=10)
        Password.insert(tk.END, password)
        tk.Button(Password_window, text='Copy',
                  command=lambda: ManOps.copy_random_password(Password_window, Password)).pack()

    def ButtonPlacementandStart(self):
        tk.Button(self.root, text="Add Details", command=self.AddWindow).pack(pady=20)
        tk.Button(self.root, text="Random Password", command=self.random_password_generator).pack()
        tk.Button(self.root, text="LookUp Details", command=self.LookUpWindow).pack(pady=20)
        tk.Button(self.root, text="Change Details", command=self.ChangePasswordWindow).pack(pady=3)
        self.root.mainloop()