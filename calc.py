import tkinter as tk


def increase():
    value = int(value_label['text'])
    value_label['text'] = str(value + 1)


def decrease():
    value = int(value_label['text'])
    value_label['text'] = str(value - 1)


window = tk.Tk().geometry('200x100')

decrease_button = tk.Button(master=window, text='-',
                            command=decrease)
decrease_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

value_label = tk.Label(master=window, text=0)
value_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

increase_button = tk.Button(master=window, text='+',
                            command=increase)
increase_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
