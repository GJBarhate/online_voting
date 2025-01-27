import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk, Image

def voteCast(root, frame1, vote, client_socket):
    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())  # Send vote to server

    message = client_socket.recv(1024)  # Receive response from server
    print(message.decode())  # Show server response in console
    message = message.decode()
    if message == "Successful":
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row=1, column=1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row=1, column=1)

    client_socket.close()


def votingPg(root, frame1, client_socket):
    root.title("Cast Your Vote")
    root.geometry("600x500")
    root.configure(bg="#2B2B2B")

    # Clear previous widgets
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Your Vote", font=('Arial', 24, 'bold'), fg="#FFD700", bg="#2B2B2B").grid(row=0, column=0, columnspan=2, pady=20)
    Label(frame1, text="", bg="#2B2B2B").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    Radiobutton(frame1, text="BJP\n\nNarendra Modi", variable=vote, value="bjp", indicator=0, height=4, width=15, command=lambda: voteCast(root, frame1, "bjp", client_socket)).grid(row=2, column=1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45, 45), Image.LANCZOS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row=2, column=0)

    Radiobutton(frame1, text="Congress\n\nRahul Gandhi", variable=vote, value="cong", indicator=0, height=4, width=15, command=lambda: voteCast(root, frame1, "cong", client_socket)).grid(row=3, column=1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((35, 48), Image.LANCZOS))
    congImg = Label(frame1, image=congLogo).grid(row=3, column=0)

    Radiobutton(frame1, text="Aam Aadmi Party\n\nArvind Kejriwal", variable=vote, value="aap", indicator=0, height=4, width=15, command=lambda: voteCast(root, frame1, "aap", client_socket)).grid(row=4, column=1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((55, 40), Image.LANCZOS))
    aapImg = Label(frame1, image=aapLogo).grid(row=4, column=0)

    Radiobutton(frame1, text="Shiv Sena\n\nUdhav Thakrey", variable=vote, value="ss", indicator=0, height=4, width=15, command=lambda: voteCast(root, frame1, "ss", client_socket)).grid(row=5, column=1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((50, 45), Image.LANCZOS))
    ssImg = Label(frame1, image=ssLogo).grid(row=5, column=0)

    Radiobutton(frame1, text="\nNOTA    \n  ", variable=vote, value="nota", indicator=0, height=4, width=15, command=lambda: voteCast(root, frame1, "nota", client_socket)).grid(row=6, column=1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((45, 35), Image.LANCZOS))
    notaImg = Label(frame1, image=notaLogo).grid(row=6, column=0)

    frame1.configure(bg="#2B2B2B")
    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('500x500')
#     frame1 = Frame(root)
#     client_socket = 'Fail'
#     votingPg(root, frame1, client_socket)
