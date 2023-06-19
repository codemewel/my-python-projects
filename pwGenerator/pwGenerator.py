import tkinter as tk
from tkinter import messagebox
import string, random, pyperclip


class mainWin:
    def __init__(self, base):
        self.base = base
        self.base.title('PW Generator')
        self.base.geometry('300x150')
        self.base.resizable(0, 0)
        self.main_frame = tk.Frame(self.base)
        self.main_frame.pack()
        self.label_name = tk.Label(self.main_frame, text='Password Generator')
        self.label_name.grid(column=0, row=0, columnspan=3, pady=5)
        self.label_name.configure(font=('Roboto Condensed', 15, 'bold'))
        self.char_label = tk.LabelFrame(self.main_frame, text='Password length')
        self.char_label.grid(column=0, row=1, columnspan=3)
        self.char_var = tk.IntVar(value=1)
        self.char_l1 = tk.Radiobutton(self.char_label, text='8 char', value=1, variable=self.char_var)
        self.char_l1.grid(column=0, row=0)
        self.char_l2 = tk.Radiobutton(self.char_label, text='12 char', value=2, variable=self.char_var)
        self.char_l2.grid(column=1, row=0)
        self.char_l3 = tk.Radiobutton(self.char_label, text='16 char', value=3, variable=self.char_var)
        self.char_l3.grid(column=2, row=0)
        self.entry_var = tk.StringVar()
        self.pw_entry = tk.Entry(self.main_frame, textvariable=self.entry_var, state='readonly')
        self.pw_entry.grid(column=0, row=2, columnspan=2)
        self.gen_btn = tk.Button(self.main_frame, text='Generate', command=self.get_char)
        self.gen_btn.grid(column=2, row=2, sticky='ew')
        self.copy_btn = tk.Button(self.main_frame, text='Copy', state=tk.DISABLED, command=self.copy_pw)
        self.copy_btn.grid(column=0, row=3, sticky='ew', columnspan=3)

    def generate_pw(self, length):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return self.password

    def get_char(self):
        self.char_val = self.char_var.get()
        if self.char_val == 1:
            self.char_length = 8
        elif self.char_val == 2:
            self.char_length = 12
        elif self.char_val == 3:
            self.char_length = 16
        self.entry_var.set(self.generate_pw(self.char_length))
        if self.entry_var.get():
            self.copy_btn.config(state=tk.NORMAL)

    def copy_pw(self):
        pyperclip.copy(self.entry_var.get())
        messagebox.showinfo(title='Copied to clipboard', message='Password copied!')


if __name__ == '__main__':
    root = tk.Tk()
    mainWin(root)
    root.mainloop()