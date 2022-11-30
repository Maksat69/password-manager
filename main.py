from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passwords():
    password_entry.delete(0, END)

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "A", "B", "C", "D", "E", "F",
               "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "-"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = "" . join(password_list)

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_file():
    web_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    data_all = {
        web_data: {
            "email": email_data,
            "passport": password_data,
        }
    }

    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="OOps", message="Dont left any field free!")
    else:
        try:
            with open("data_dow.json", mode="r") as file_data:
                data = json.load(file_data)

        except FileNotFoundError:
            with open("data_dow.json", mode="w") as file_data:
                json.dump(data_all, file_data, indent=4)

        else:
            data.update(data_all)
            with open("data_dow.json", mode="w") as file_data:
                json.dump(data, file_data, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


def search_file():
    website = website_entry.get()
    try:
        with open("data_dow.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no data exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["passport"]
            messagebox.showinfo(title=website, message=f"your email: {email} \n your password: {password}")
        else:
            messagebox.showinfo(title="OOps", message="There is no such website exist")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My passport generate")
window.config(pady=50, padx=50)

logo_photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_photo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Your Email here")  # Write Your email here to provide it every time you use app
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)



# Buttons
generate_password_button = Button(text="Generate Password", command=passwords)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=39, command=add_file)
add_button.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=15, command=search_file)
search.grid(row=1, column=2)



window.mainloop()
