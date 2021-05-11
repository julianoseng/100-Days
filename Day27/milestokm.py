from tkinter import *

def button_calculation():
    miles = float(miles_input.get())
    calculated_km = miles * 1.609
    kilometer_int_label.config(text=calculated_km)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=30, pady=30)

# Entry box for user to input miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 18))
miles_label.grid(column=2, row=0)

# is equal to Label
is_equal_label = Label(text="is equal to", font=("Arial", 18))
is_equal_label.grid(column=0, row=1)

# Kilometer integer Label
kilometer_int_label = Label(text=0, font=("Arial", 18))
kilometer_int_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 18))
km_label.grid(column=2, row=1)

# Calculate Button
calculate_button = Button(text="Calculate", command=button_calculation)
calculate_button.grid(column=1, row=3)

window.mainloop()