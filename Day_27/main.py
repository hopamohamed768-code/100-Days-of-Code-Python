import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=30, pady=30)

# Label
is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(row=1, column=0)
miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=2)
km_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(row=1, column=2)
km_result_label = tkinter.Label(text="0", font=("Arial", 12, "bold"))
km_result_label.grid(row=1, column=1)


#Button

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60
    km_result_label.config(text=f"{km}")

    

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)


#Entry

miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)

























window.mainloop()