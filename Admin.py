import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
from tkinter import *
from registerVoter import *
from admFunc import *


def AdminHome(root,frame1,frame3):
    root.title("Admin")
    root.geometry("700x600")
    root.config(bg="#f4f4f9")
    
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame3, text="Admin", command = lambda: AdminHome(root, frame1, frame3), font=('Arial', 12), bg='#4CAF50', fg='white').grid(row = 1, column = 0)
    frame3.pack(side=TOP, pady=20)

    Label(frame1, text="Admin", font=('Helvetica', 25, 'bold'), fg='#333333', bg='#f4f4f9').grid(row = 0, column = 1)
    Label(frame1, text="").grid(row = 1,column = 0)

  # Admin functionalities
    runServer = Button(frame1, text="Run Server", width=20, height=2, command=lambda: sb_p.call('start python Server.py', shell=True), font=('Arial', 12), bg='#2196F3', fg='white')
    registerVoter = Button(frame1, text="Register Voter", width=20, height=2, command=lambda: regV.Register(root, frame1), font=('Arial', 12), bg='#FF9800', fg='white')
    showVotes = Button(frame1, text="Show Votes", width=20, height=2, command=lambda: adFunc.showVotes(root, frame1), font=('Arial', 12), bg='#009688', fg='white')
    reset = Button(frame1, text="Reset Data", width=20, height=2, command=lambda: adFunc.resetAll(root, frame1), font=('Arial', 12), bg='#E91E63', fg='white')

    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)
    Label(frame1, text="").grid(row = 6,column = 0)
    Label(frame1, text="").grid(row = 8,column = 0)
    runServer.grid(row = 3, column = 1, columnspan = 2)
    registerVoter.grid(row = 5, column = 1, columnspan = 2)
    showVotes.grid(row = 7, column = 1, columnspan = 2)
    # reset.grid(row = 9, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def log_admin(root,frame1,admin_ID,password):

    if(admin_ID=="Admin" and password=="admin"):
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect", width=500)
        msg.grid(row = 6, column = 0, columnspan = 5)


def AdmLogin(root,frame1):

    root.title("Admin Login")
    root.geometry("600x400")
    root.config(bg="#f4f4f9")

    for widget in frame1.winfo_children():
        widget.destroy()

   # Login Header
    Label(frame1, text="Admin Login", font=('Helvetica', 24, 'bold'), fg='#333333', bg='#f4f4f9').grid(row=0, column=1, columnspan=2, pady=30)

    # Admin ID and Password fields
    Label(frame1, text="Admin ID:", anchor="e", justify=LEFT, font=('Arial', 12), bg='#f4f4f9').grid(row=1, column=0, pady=10)
    Label(frame1, text="Password:", anchor="e", justify=LEFT, font=('Arial', 12), bg='#f4f4f9').grid(row=2, column=0, pady=10)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = admin_ID)
    e1.grid(row = 2,column = 2)
    e2 = Entry(frame1, textvariable = password, show = '*')
    e2.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=15, height=2, command=lambda: log_admin(root, frame1, admin_ID.get(), password.get()), font=('Arial', 12), bg='#4CAF50', fg='white')
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         frame3 = Frame(root)
#         AdminHome(root,frame1,frame3)
