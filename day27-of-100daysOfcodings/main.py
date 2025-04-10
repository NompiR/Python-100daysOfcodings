from tkinter import *

window= Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=30, pady=50)


def convert_mile_to_kms():
    one_miles = 1.60934
    inputs = float(type_input_miles.get())
    converts = inputs * one_miles
    #or use round(inputs * one_miles) convert float to int
    text_miles_to_km_number.config(text= int(converts))




type_input_miles = Entry(width=15, bd=2)
#y = Entry()
type_input_miles.grid(column=2, row=1)

text_miles = Label(text="Miles", font=("Arial", 15))
text_miles.grid(column=3, row=1)

text_miles_equal_to = Label(text="is equal to", font=("Arial", 15))
text_miles_equal_to.grid(column=1, row=2)

text_miles_to_km_number = Label(text="0", font=("Arial", 15))
text_miles_to_km_number.grid(column=2, row=2)


text_miles_to_km = Label(text="Km", font=("Arial", 15))
text_miles_to_km.grid(column=3, row=2)


convert_miles_to_km_button = Button(text="Calculate", justify="center", width=10, height=1, font=("Arial", 10), bd=2, command=convert_mile_to_kms)
convert_miles_to_km_button.grid(column=2, row=3)


window.mainloop()
