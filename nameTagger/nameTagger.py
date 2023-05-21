import re
import tkinter as tk
from tkinter import messagebox


class MainWindow:
    def __init__(self, base):
        self.base = base
        self.base.title('Nametagger')
        self.base.minsize(300,150)
        self.base.resizable(0,0)
        self.main_frame = tk.Frame(self.base)
        self.main_frame.pack()
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.confirm_fname = tk.StringVar()
        self.confirm_fname.trace_variable('w', self.validate_name)
        self.confirm_lname = tk.StringVar()
        self.confirm_lname.trace_variable('w', self.validate_name)
        self.main_label = tk.LabelFrame(self.main_frame, text='Enter Information')
        self.main_label.pack(pady=20, padx=20)
        self.fname_label = tk.Label(self.main_label, text='Firstname:')
        self.fname_label.grid(column=0, row=0, pady=(10, 0))
        self.fname_entry = tk.Entry(self.main_label, textvariable=self.confirm_fname)
        self.fname_entry.grid(column=1, row=0, padx=(0,5), pady=(10, 0))
        self.fname_entry.focus()
        self.lname_label = tk.Label(self.main_label, text='Lastname:')
        self.lname_label.grid(column=0, row=1, pady=(0, 5))
        self.lname_entry = tk.Entry(self.main_label, textvariable=self.confirm_lname)
        self.lname_entry.grid(column=1, row=1, padx=(0,5))
        self.prompt_label = tk.Label(self.main_label, text='Please provide details.')
        self.prompt_label.grid(column=0, row=2, columnspan=2)
        self.ntag_btn = tk.Button(self.main_label, text='Tag It!', command=self.nametag)
        self.ntag_btn.grid(column=1, row=3, pady=(5, 10))

    def validate_name(self, *args):
        self.lname_var = self.confirm_lname.get()
        self.fname_var = self.confirm_fname.get()
        if len(self.fname_var) >= 14 or len(self.lname_var) >= 14:
            self.prompt_label.config(text='Max characters is 14!', foreground='red')
        elif re.search(r'\d', self.fname_var) or re.search(r'\d', self.lname_var):
            self.prompt_label.config(text='No numbers allowed!', foreground='red')
        elif re.search(r'[^\w\s ]', self.fname_var) or re.search(r'[^\w\s]', self.lname_var):
            self.prompt_label.config(text='Invalid character', foreground='red')
        elif re.search(r'^ +', self.fname_var) or re.search(r'^ +', self.lname_var):
            self.prompt_label.config(text='Check your spaces!', foreground='red')
        elif not self.fname_var and self.lname_var:
            self.prompt_label.config(text='Your Firstname please?', foreground='orange')
        elif not self.lname_var and self.fname_var:
            self.prompt_label.config(text='Forgot your Lastname?', foreground='orange')
        elif not self.fname_var and not self.lname_var:
            self.prompt_label.config(text='All details missing!', foreground='red')
        else:
            self.prompt_label.config(text='Looking good!', foreground='green')
            return True

    def nametag(self):
        if self.validate_name():
            messagebox.showinfo(title='Welcome!', message='Welcome! {} {[0]}.'.format(self.fname_var, self.lname_var))
        else:
            messagebox.showerror(title='Ooppss!', message='Please check details.')


if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()