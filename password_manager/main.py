from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT = ("Courier", 12, "normal")
DEFAULT_EMAIL = "example@email.com"
FILE_NAME = "data.json"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    passwd_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, string=DEFAULT_EMAIL)

    password_letters = [choice(alphabet) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    passwd = "".join(password_list)
    passwd_entry.insert(0, passwd)
    pyperclip.copy(passwd)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        with open(FILE_NAME, mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="You don't have any saved passwords")
    else:
        website = website_entry.get()
        if website in data:
            passwd = data[website]["password"]
            username = data[website]["email"]
            pyperclip.copy(passwd)
            messagebox.showinfo(title=f"Data for {website}", message=f"Username: {username}\nPassword: {passwd}")
        else:
            messagebox.showinfo(title=f"Search result",
                                message=f"Website {website} wasn't found in data")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = username_entry.get()
    passwd = passwd_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": passwd,
        }
    }

    if website == "" or username == "" or passwd == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n "
                                                          f"Email: {username}\n Password: {passwd}\n"
                                                          f"It ok to save?")
        if is_ok:
            try:
                with open(FILE_NAME, mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(FILE_NAME, mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open(FILE_NAME, mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                passwd_entry.delete(0, END)
                username_entry.delete(0, END)
                username_entry.insert(0, string=DEFAULT_EMAIL)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_txt = Label(text="Website:", font=FONT)
website_txt.grid(row=1, column=0)
username_txt = Label(text="Email/Username:", font=FONT)
username_txt.grid(row=2, column=0)
passwd_txt = Label(text="Password:", font=FONT)
passwd_txt.grid(row=3, column=0)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=51)
username_entry.insert(END, string=DEFAULT_EMAIL)
username_entry.grid(row=2, column=1, columnspan=2)
passwd_entry = Entry(width=32)
passwd_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search", width=14, command=search_website)
search_btn.grid(row=1, column=2)
passwd_btn = Button(text="Generate Password", command=generate_passwd)
passwd_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=43, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
