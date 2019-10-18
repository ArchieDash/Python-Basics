import tkinter as tk


window = tk.Tk()
window.title("Address Entry Form")

main_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
main_frame.pack()

fname_label = tk.Label(master=main_frame, text='First Name: ')
fname_label.grid(row=0, column=0, sticky=tk.E)
fname_entry = tk.Entry(master=main_frame, width=50)
fname_entry.grid(row=0, column=1)

lname_label = tk.Label(master=main_frame, text='Last Name: ')
lname_label.grid(row=1, column=0, sticky=tk.E)
lname_entry = tk.Entry(master=main_frame, width=50)
lname_entry.grid(row=1, column=1)

address1_entry_label = tk.Label(master=main_frame, text='Address Line 1: ')
address1_entry_label.grid(row=2, column=0, sticky=tk.E)
address1_entry = tk.Entry(master=main_frame, width=50)
address1_entry.grid(row=2, column=1)

address2_entry_label = tk.Label(master=main_frame, text='Address Line 2: ')
address2_entry_label.grid(row=3, column=0, sticky=tk.E)
address2_entry = tk.Entry(master=main_frame, width=50)
address2_entry.grid(row=3, column=1)

city_entry_label = tk.Label(master=main_frame, text='City: ')
city_entry_label.grid(row=4, column=0, sticky=tk.E)
city_entry = tk.Entry(master=main_frame, width=50)
city_entry.grid(row=4, column=1)

state_entry_label = tk.Label(master=main_frame, text='State/Province: ')
state_entry_label.grid(row=5, column=0, sticky=tk.E)
state_entry = tk.Entry(master=main_frame, width=50)
state_entry.grid(row=5, column=1)

postal_entry_label = tk.Label(master=main_frame, text='Postal Code: ')
postal_entry_label.grid(row=6, column=0, sticky=tk.E)
postal_entry = tk.Entry(master=main_frame, width=50)
postal_entry.grid(row=6, column=1)

country_entry_label = tk.Label(master=main_frame, text='Country: ')
country_entry_label.grid(row=7, column=0, sticky=tk.E)
country_entry = tk.Entry(master=main_frame, width=50)
country_entry.grid(row=7, column=1)

button_frame = tk.Frame()
button_frame.pack(fill=tk.X, ipadx=5, ipady=5)

submit_button = tk.Button(master=button_frame, text='Submit')
submit_button.pack(side=tk.RIGHT, padx=10, ipadx=10)

clear_button = tk.Button(master=button_frame, text='Clear', command=clear_fields)
clear_button.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()
