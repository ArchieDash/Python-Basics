import tkinter as tk


def celsius_to_fahrenheit(celsius):
    fahrenheit = round(float(celsius) * 9/5 + 32, 2)
    return fahrenheit


def convert():
    celsius = celsius_entry.get()
    try:
        result = str(celsius_to_fahrenheit(celsius))
    except ValueError:
        result = 'Invalid'
    result_display.config(text=result)


window = tk.Tk()
window.title('Temperature Converter')
window.resizable(width=False, height=False)

conversion_frame = tk.Frame(master=window)
conversion_frame.pack(side=tk.LEFT, padx=5, pady=5)

button_frame = tk.Frame(master=window)
button_frame.pack(side=tk.LEFT, padx=5, pady=5)

celsius_entry_label = tk.Label(master=conversion_frame,
                               text='Degrees (Celsius):')
celsius_entry_label.grid(row=0, column=0)

celsius_entry = tk.Entry(master=conversion_frame)
celsius_entry.grid(row=0, column=1)

result_label = tk.Label(master=conversion_frame,
                        text='Degrees (Fahrenheit):')
result_label.grid(row=1, column=0)

result_display = tk.Label(master=conversion_frame)
result_display.grid(row=1, column=1)

convert_button = tk.Button(master=button_frame,
                           text='Convert', command=convert)
convert_button.pack(side=tk.LEFT)

window.mainloop()
            
