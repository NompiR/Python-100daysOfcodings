from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    input_pass.get()

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbol = [choice(symbols) for _ in range(nr_symbols)]
    password_number = [choice(numbers) for _ in range(nr_numbers)]

    password_gen = password_number + password_symbol + password_letter
    shuffle(password_gen)

    your_pass = "".join(password_gen)

    print(f"Your password is: {your_pass}")
    input_pass.insert(0, your_pass)

    pyperclip.copy(your_pass)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_website = input_website.get()
    try:
        with open("data.json") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if search_website in data:
            email_id = data[search_website]['email']
            pass_id = data[search_website]['password']
            messagebox.showinfo(title=search_website, message= f"Email: {email_id} \n Password: {pass_id}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_website} exists.")


        """
        for key in data.keys():
            if key == search_website:
                print("yes")
            else:
                print("No")"""


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    get_website = input_website.get()
    get_email = input_email.get()
    get_pass = input_pass.get()
    new_data = {
        get_website: {
            "email": get_email,
            "password": get_pass,
        }
    }

    if len(get_website) <= 0 or len(get_pass) <= 0:
        messagebox.showinfo(title="Oops..", message="Please make sure you haven't left any fields empty.")
    else:
        #is_ok = messagebox.askokcancel(title=get_website, message=f"These are the details entered: \nEmail: {get_email}"
        #f"\nPassword: {get_pass} \nIs it ok to save?")

        #if is_ok:
            #f = open("data.txt", "a")
            #f.write(f"{get_website} / {get_email} / {get_pass} \n")
            #f.close()

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#window.minsize(width=300, height=300)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels

label_website = Label(text="Website:", font=("Arial", 12))
label_website.grid(column= 0, row= 1)

label_email = Label(text="Email/Username:", font=("Arial", 12))
label_email.grid(column=0, row=2)

label_password = Label(text="Password:", font=("Arial", 12))
label_password.grid(column=0, row=3)

#Inputs

input_website = Entry(width=22)
input_website.grid(column=1, row= 1)
input_website.focus()

input_email = Entry(width=40)
input_email.grid(column=1, row= 2, columnspan=2)
input_email.insert(0, "nompi@mail.com")

input_pass = Entry(width=22)
input_pass.grid(column=1, row= 3)
#input_pass.insert(0, password_generate())

#Buttons
generate_search = Button(text="Search", width=10, command=find_password)
generate_search.grid(column=2, row=1, columnspan=2)

generate_pass = Button(text="Generate Password", command=password_generate)
generate_pass.grid(column=2, row= 3)

add_pass = Button(text="Add", width=36, command=save)
add_pass.grid(column=1, row= 4, columnspan=2)




window.mainloop()
