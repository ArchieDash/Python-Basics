import tkinter as tk
from tkinter import filedialog

def clear_text_box():
    text_box.delete(1.0, tk.END)
    window.title('Text Editor')


def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[('Text Files', '.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    clear_text_box()
    with open(filepath, 'r') as file:
        text_box.insert(tk.END, file.read())
    window.title(f'Text Editor - {filepath}')


def save_file_as():
    filepath = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text File', '.txt')]
        )
    if not filepath:
        return
    with open(filepath, 'w') as file:
        file.write(text_box.get(1.0, tk.END))
    window.title(f'Text Editor - {filepath}')


window = tk.Tk()
window.title('Text Editor')
window.geometry('800x800')

button_frame = tk.Frame(master=window, width=50)
button_frame['relief'] = tk.GROOVE
button_frame['borderwidth'] = 2
button_frame.pack(side=tk.LEFT, fill=tk.Y)

editor_frame = tk.Frame(master=window)
editor_frame['relief'] = tk.GROOVE
editor_frame['borderwidth'] = 2
editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

open_button = tk.Button(master=button_frame)
open_button['text'] = 'Open'
open_button.pack(fill=tk.X, padx=5, pady=5)
open_button['command'] = open_file

save_as_button = tk.Button(master=button_frame)
save_as_button['text'] = 'Save As...'
save_as_button.pack(fill=tk.X, padx=5, pady=5)
save_as_button['command'] = save_file_as

clear_button = tk.Button(master=button_frame)
clear_button['text'] = 'Clear'
clear_button.pack(fill=tk.X, padx=5, pady=5)
clear_button['command'] = clear_text_box

text_box = tk.Text(master=editor_frame)
text_box.pack(fill=tk.BOTH, expand=True)

window.mainloop()
