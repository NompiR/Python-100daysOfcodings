import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#Button component

def button_clicked():
    #label= tkinter.Label(text="Button Got Clicked", font=("Arial", 22))
    #label.pack()
    #OR use config func
    #my_label.config(text="Button Got Clicked")

    #input display text on the screen
    ip = input_entry.get()
    my_label.config(text=ip)

button = tkinter.Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)



#Entry component is an input function
input_entry = tkinter.Entry(width=10)
input_entry.grid(column=3, row=2)




window.mainloop()
