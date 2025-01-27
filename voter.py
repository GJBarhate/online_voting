import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
import tkinter as tk
from tkinter import ttk

# Function to establish connection to the server
def establish_connection():
    try:
        host = socket.gethostname()  # Use appropriate IP if needed
        port = 4001  # Ensure this port matches the server's port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Connected to server: {client_socket}")
        message = client_socket.recv(1024)  # Connection establishment message
        if message.decode() == "Connection Established":
            return client_socket
        else:
            return 'Failed'
    except Exception as e:
        print(f"Connection Failed, check if server is running... {e}")
        return 'Failed'


# Function to handle the failed login attempt
def failed_return(root, frame1, client_socket, message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Helvetica', 14, 'bold'),fg="red").grid(row=1, column=1)
    try:
        client_socket.close()
    except:
        return


# Function to send voter credentials to the server
def log_server(root, frame1, client_socket, voter_ID, password):
    if not (voter_ID and password):
        voter_ID = "0"
        password = "x"
    
    message = f"{voter_ID} {password}"
    print(f"Sending credentials: {message}")  # Debugging line
    client_socket.send(message.encode())  # Send credentials to server

    message = client_socket.recv(1024)  # Authentication response
    message = message.decode()

    if message == "Authenticate":
        votingPg(root, frame1, client_socket)
    elif message == "VoteCasted":
        message = "Vote has Already been Cast"
        failed_return(root, frame1, client_socket, message)
    elif message == "InvalidVoter":
        message = "Invalid Voter"
        failed_return(root, frame1, client_socket, message)
    else:
        message = "Server Error"
        failed_return(root, frame1, client_socket, message)


# Function to handle the login window

def voterLogin(root, frame1):
    client_socket = establish_connection()
    if client_socket == 'Failed':
        failed_return(root, frame1, client_socket, "Connection failed")
        return

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    # Add styles for a modern look
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 14))
    style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="white", background="#4CAF50")
    style.configure("TEntry", font=("Helvetica", 12))

    # Title
    ttk.Label(frame1, text="Voter Login", font=("Helvetica", 20, "bold"), foreground="#4CAF50").pack(pady=10)

    # Voter ID Field
    voter_ID = tk.StringVar()
    ttk.Label(frame1, text="Voter ID:", font=("Helvetica", 14)).pack(anchor="w", padx=20)
    ttk.Entry(frame1, textvariable=voter_ID, font=("Helvetica", 14), width=30).pack(pady=5)

    # Password Field
    password = tk.StringVar()
    ttk.Label(frame1, text="Password:", font=("Helvetica", 14)).pack(anchor="w", padx=20)
    ttk.Entry(frame1, textvariable=password, font=("Helvetica", 14), width=30, show="*").pack(pady=5)

    # Submit Button
    ttk.Button(
        frame1, text="Login", style="TButton", command=lambda: log_server(root, frame1, client_socket, voter_ID.get(), password.get())
    ).pack(pady=20)

    # Frame Packing
    frame1.pack(pady=20, padx=20, fill="both", expand=True)
    root.mainloop()



# Uncomment below to run the application
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('500x500')
#     frame1 = Frame(root)
#     voterLogin(root, frame1)
