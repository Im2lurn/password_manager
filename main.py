from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        file = open('text.json', 'r')
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        messagebox.showinfo(title='NO FILE', message='No data file found')

    else:
        if ip1.get() in data:
            messagebox.showinfo(title='DATA FOUND', message=data[ip1.get()])
        else:
            messagebox.showinfo(title='NO INFO', message='No details for the website exist.')
        file.close()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    ip3.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to your password generator!")
    nletters = random.randint(8, 10)
    nsymbols = random.randint(2, 4)
    nnumbers = random.randint(2, 4)

    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    password1 = [random.choice(letters) for x in range(0, nletters)]

    password2 = [random.choice(symbols) for x in range(0, nsymbols)]

    password3 = [random.choice(numbers) for x in range(0, nnumbers)]

    password = password1 + password2 + password3

    # shuffing list to make strong password
    random.shuffle(password)
    # coverting list to string and temporary text insertion
    ip3.insert(0, f"{''.join(password)}")
    pyperclip.copy(''.join(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    # dictionary to add to json file
    new_data = {
        ip1.get(): {
            'email': ip2.get(),
            'password': ip3.get()
        }
    }

    if len(ip1.get()) and len(ip3.get()):

        try:
            file = open('text.json', 'r')
            data = json.load(file)
        except FileNotFoundError:
            # if file is initially empty
            file = open('text.json', 'w')
            json.dump(new_data, file, indent=4)
            # indent allows to give indentation in the json file
            # makes it more readable
        else:
            data.update(new_data)
            # reading old data
            file = open('text.json', 'w')
            json.dump(data, file, indent=4)
        finally:
            file.close()

        # clear text
        ip1.delete(0, END)
        ip3.delete(0, END)

        # shift focus back to ip1
        ip1.focus()

    else:
        messagebox.showwarning(title="warning", message='website or password field cannot be empty')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

ip1 = Entry(width=21)
ip1.grid(column=1, row=1, sticky="EW")
# makes sure the cursor is already present in the first text box
ip1.focus()

ip2 = Entry(width=35)
ip2.grid(column=1, row=2, columnspan=2, sticky="EW")
# temporary text insertion
ip2.insert(0, "ishita16gupta@gmail.com")

ip3 = Entry(width=21)
ip3.grid(column=1, row=3, sticky="EW")

button1 = Button(text='Generate Password', command=generate_password)
button1.grid(column=2, row=3, sticky="EW")

button2 = Button(text='Add', width=36, command=add_to_file)
button2.grid(column=1, row=4, columnspan=2, sticky="EW")

button3 = Button(text='Search', command=find_password)
button3.grid(column=2, row=1, sticky='EW')
window.mainloop()
