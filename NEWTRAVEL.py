# Creator   Mohammed Al-Bunde
# Date      2023-02-15
# Project   Flight Search
# Version   1.0.0
import tkinter as tk
import webbrowser
from tkcalendar import Calendar, DateEntry

def submit():
    origin = origin_entry.get()
    destination = dest_entry.get()
    flight_type = var.get()
    travel_date = date_entry.get_date().strftime('%Y-%m-%d')
    if flight_type == "round-trip":
        return_date = return_entry.get_date().strftime('%Y-%m-%d')
        url = f"https://www.google.com/flights?hl=en#flt={origin}.{destination}.{travel_date}*" \
              f"{destination}.{origin}.{return_date}"
    else:
        url = f"https://www.google.com/flights?hl=en#flt={origin}.{destination}.{travel_date}"
    webbrowser.open_new_tab(url)

def show_return():
    if var.get() == "round-trip":
        return_label.grid(row=3, column=0, padx=5, pady=5)
        return_entry.grid(row=3, column=1, padx=5, pady=5)
    else:
        return_label.grid_forget()
        return_entry.grid_forget()

def choose_date(entry):
    def get_date():
        date = cal.selection_get().strftime('%Y-%m-%d')
        entry.delete(0, tk.END)
        entry.insert(0, date)
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode="day", year=2022, month=1, day=1)
    cal.pack(padx=5, pady=5)
    button = tk.Button(top, text="OK", command=get_date)
    button.pack(padx=5, pady=5)

root = tk.Tk()
root.title("Flight Search")

# Labels
origin_label = tk.Label(root, text="Origin:")
origin_label.grid(row=0, column=0, padx=5, pady=5)
dest_label = tk.Label(root, text="Destination:")
dest_label.grid(row=1, column=0, padx=5, pady=5)
date_label = tk.Label(root, text="Travel Date:")
date_label.grid(row=2, column=0, padx=5, pady=5)

# Entry fields
origin_entry = tk.Entry(root)
origin_entry.grid(row=0, column=1, padx=5, pady=5)
dest_entry = tk.Entry(root)
dest_entry.grid(row=1, column=1, padx=5, pady=5)
date_entry = DateEntry(root, date_pattern='yyyy-mm-dd', width=12, background='darkblue', foreground='white', borderwidth=2, command=lambda: choose_date(date_entry))
date_entry.grid(row=2, column=1, padx=5, pady=5)

# One Way or Round Trip Radio Buttons
var = tk.StringVar()
one_way_radio = tk.Radiobutton(root, text="One Way", variable=var, value="one-way", command=show_return)
one_way_radio.grid(row=3, column=0, padx=5, pady=5)
round_trip_radio = tk.Radiobutton(root, text="Round Trip", variable=var, value="round-trip", command=show_return)
round_trip_radio.grid(row=4, column=0, padx=5, pady=5)
var.set("one-way") # One Way is the default value

# Return date entry field 
return_label = tk.Label(root, text="Return Date:")
return_entry = DateEntry(root, date_pattern='yyyy-mm-dd', width=12, background='darkblue', foreground='white', borderwidth=2)
return_label.grid(row=3, column=0, padx=5, pady=5)
return_entry.grid(row=3, column=1, padx=5, pady=5)
return_label.grid_remove()
return_entry.grid_remove()

def show_return():
    if var.get() == "round-trip":
        return_label.grid()
        return_entry.grid()
    else:
        return_label.grid_remove()
        return_entry.grid_remove()
show_return() # Show or hide the return date entry based on the initial value of the flight type radio buttons

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
