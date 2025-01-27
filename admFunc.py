import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import dframe as df

def reset_all(root, frame):
    try:
        # Uncomment these lines if the reset logic is implemented in `dframe`
        # df.count_reset()
        # df.reset_voter_list()
        # df.reset_cand_list()

        Label(frame, text="").grid(row=10, column=0)
        msg = Message(frame, text="All data has been successfully reset!", width=500, fg="green",bg="#f2f2f2", font=('Helvetica', 12, 'bold'))
        msg.grid(row=11, column=0, columnspan=5)
    except Exception as e:
        msg = Message(frame, text=f"Error: {str(e)}", width=500, fg="red", font=("Arial", 10, "italic"))
        msg.grid(row=11, column=0, columnspan=5)

def showVotes(root, frame):
    try:
        # Fetch results from the data frame
        results = df.show_result()
        if not results:
            raise ValueError("No results available. Please ensure voting data exists.")

        root.title("Election Results")
        for widget in frame.winfo_children():
            widget.destroy()

        # Add a title
        Label(frame, text="Election Results", font=("Helvetica", 18, "bold"), fg="#0033A0").grid(row=0, column=1, rowspan=1)
        Label(frame, text="").grid(row=1, column=0)

        # Dictionary for dynamic UI element generation
        parties = {
            "bjp": {"name": "BJP", "image": "img/bjp.png"},
            "cong": {"name": "Congress", "image": "img/cong.png"},
            "aap": {"name": "AAP", "image": "img/aap.png"},
            "ss": {"name": "Shiv Sena", "image": "img/ss.png"},
            "nota": {"name": "NOTA", "image": "img/nota.png"}
        }

        row = 2
        for key, details in parties.items():
            try:
                # Load party logos dynamically
                logo = ImageTk.PhotoImage(Image.open(details["image"]).resize((40, 40), Image.LANCZOS))
                Label(frame, image=logo).grid(row=row, column=0)
                # Keep a reference to avoid garbage collection of images
                frame.image = logo
            except FileNotFoundError:
                Label(frame, text="(Image Missing)", fg="red").grid(row=row, column=0)

            # Add party name and vote count
            Label(frame, text=f"{details['name']}:", font=("Arial", 12, "bold")).grid(row=row, column=1)
            Label(frame, text=results.get(key, "N/A"), font=("Arial", 12)).grid(row=row, column=2)

            row += 1

        frame.pack()
    except Exception as e:
        Label(frame, text=f"Error: {str(e)}", fg="red", font=("Arial", 12)).grid(row=2, column=0, columnspan=3)

# Uncomment for testing purposes
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('500x500')
#     frame = Frame(root)
#     display_results(root, frame)
#     root.mainloop()
