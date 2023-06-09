import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, filedialog
from datetime import datetime
import pyperclip
import os


class mainWin:
    def __init__(self, base):
        self.base = base
        self.base.title('callNoter X')
        self.base.minsize(360, 600)
        self.base.resizable(0, 0)
        self.main_frame = tk.Frame(self.base)
        self.main_frame.pack()
        self.main_frame.columnconfigure(0, weight=1)
        self.confirm_name = tk.StringVar()
        self.confirm_phone = tk.StringVar()
        self.confirm_email = tk.StringVar()
        self.confirm_region = tk.StringVar()
        self.confirm_isp = tk.StringVar()
        self.confirm_model = tk.StringVar()
        self.confirm_pop = tk.StringVar()
        self.confirm_dop = tk.StringVar()
        self.confirm_issue = tk.StringVar()
        self.confirm_wf = tk.StringVar()
        self.cx_label = tk.LabelFrame(self.main_frame, text='Customer Info')
        self.cx_label.grid(column=0, row=0, ipadx=5, ipady=5)
        self.name_label = tk.Label(self.cx_label, text='Name:')
        self.name_label.grid(column=0, row=0)
        self.name_entry = tk.Entry(self.cx_label, textvariable=self.confirm_name)
        self.name_entry.grid(column=1, row=0)
        self.phone_label = tk.Label(self.cx_label, text='Phone:')
        self.phone_label.grid(column=0, row=1)
        self.phone_entry = tk.Entry(self.cx_label, textvariable=self.confirm_phone)
        self.phone_entry.grid(column=1, row=1)
        self.email_label = tk.Label(self.cx_label, text='Email:')
        self.email_label.grid(column=0, row=2)
        self.email_entry = tk.Entry(self.cx_label, textvariable=self.confirm_email)
        self.email_entry.grid(column=1, row=2)
        self.region_label = tk.Label(self.cx_label, text='Region:')
        self.region_label.grid(column=2, row=0)
        self.region_entry = tk.Entry(self.cx_label, textvariable=self.confirm_region)
        self.region_entry.grid(column=3, row=0)
        self.isp_label = tk.Label(self.cx_label, text='ISP:')
        self.isp_label.grid(column=2, row=1)
        self.isp_entry = tk.Entry(self.cx_label, textvariable=self.confirm_isp)
        self.isp_entry.grid(column=3, row=1)
        self.dev_label = tk.LabelFrame(self.main_frame, text='Device Info')
        self.dev_label.grid(column=0, row=1, ipadx=12, ipady=5)
        self.model_label = tk.Label(self.dev_label, text='Model:')
        self.model_label.grid(column=0, row=0)
        self.model_entry = tk.Entry(self.dev_label, textvariable=self.confirm_model)
        self.model_entry.grid(column=1, row=0)
        self.pop_label = tk.Label(self.dev_label, text='POP:')
        self.pop_label.grid(column=2, row=0)
        self.pop_entry = tk.Entry(self.dev_label, textvariable=self.confirm_pop)
        self.pop_entry.grid(column=3, row=0)
        self.dop_label = tk.Label(self.dev_label, text='DOP:')
        self.dop_label.grid(column=2, row=1)
        self.dop_entry = tk.Entry(self.dev_label, textvariable=self.confirm_dop)
        self.dop_entry.grid(column=3, row=1)
        self.sop_label = tk.LabelFrame(self.main_frame, text='SOP')
        self.sop_label.grid(column=0, row=2, ipadx=4, ipady=5)
        self.issue_label = tk.Label(self.sop_label, text='Issue:')
        self.issue_label.grid(column=0, row=0)
        self.issue_entry = tk.Entry(self.sop_label, textvariable=self.confirm_issue)
        self.issue_entry.grid(column=1, row=0, sticky='w')
        self.wf_label = tk.Label(self.sop_label, text='Workflow:')
        self.wf_label.grid(column=2, row=0)
        self.wf_entry = tk.Entry(self.sop_label, width=10, textvariable=self.confirm_wf)
        self.wf_entry.grid(column=3, row=0, sticky='w')
        self.ts_label = tk.Label(self.sop_label, text='Troubleshooting:')
        self.ts_label.grid(column=0, row=1, columnspan=2, sticky='w', pady=(5, 1))
        self.ts_entry = ScrolledText(self.sop_label, height=10, width=40)
        self.ts_entry.grid(column=0, row=2, columnspan=4)
        self.ts_entry.bind('<Control-a>', self.select_all)
        self.copy_btn = tk.Button(self.main_frame, text='Copy All', command=self.copy_all)
        self.copy_btn.grid(column=0, row=3, sticky='ew')
        self.notes_label = tk.LabelFrame(self.main_frame, text='Additional Info')
        self.notes_label.grid(column=0, row=5, pady=(10, 5), ipadx=4, ipady=5)
        self.notes_entry = ScrolledText(self.notes_label, height=5, width=40)
        self.notes_entry.grid(column=0, row=0, columnspan=4)
        self.notes_entry.bind('<Control-a>', self.select_all)
        self.save_btn = tk.Button(self.main_frame, text='Save', width=10, command=self.save_info)
        self.save_btn.grid(column=0, row=6, sticky='w')
        self.clear_btn = tk.Button(self.main_frame, text='Clear', width=10, command=self.clear_entries)
        self.clear_btn.grid(column=0, row=6, sticky='e')
        self.set_btn = tk.Button(self.main_frame, text='Settings', width=10, command=self.settings)
        self.set_btn.grid(column=0, row=7, sticky='w')
        self.author = tk.Label(self.main_frame, text='Powered by code Me Wel')
        self.author.grid(column=0, row=8, pady=(10, 0))
        self.set_dir = 'C:/callNoterX/'
        self.set_file = 'settings.txt'
        self.f_dir = self.set_dir + self.set_file

    def get_val(self):
        self.name_var = self.confirm_name.get()
        self.phone_var = self.confirm_phone.get()
        self.email_var = self.confirm_email.get()
        self.region_var = self.confirm_region.get()
        self.isp_var = self.confirm_isp.get()
        self.model_var = self.confirm_model.get()
        self.pop_var = self.confirm_pop.get()
        self.dop_var = self.confirm_dop.get()
        self.issue_var = self.confirm_issue.get()
        self.wf_var = self.confirm_wf.get()
        self.ts_var = self.ts_entry.get('1.0', tk.END)
        self.all_info = 'Name: {}\nPhone: {}\nEmail: {}\nRegion: {}\nISP: {}\nModel: {}\nPOP: {}\nDOP: {}\nIssue: {' \
                        '}\nWorkflow: {}\nTroubleshooting:\n{}'.format(
            self.name_var, self.phone_var, self.email_var, self.region_var, self.isp_var, self.model_var, self.pop_var,
            self.dop_var, self.issue_var, self.wf_var, self.ts_var)
        return self.all_info

    def select_all(self, event):
        self.event = event
        self.event.widget.tag_add('sel', '1.0', 'end')
        return 'break'

    def copy_all(self, *args):
        pyperclip.copy(self.get_val())
        messagebox.showinfo(title='Copied to clipboard', message='Information copied!')

    def clear_entries(self):
        self.clear_prompt = messagebox.askyesno(title='Hey wait!', message='Are you sure you want to clear all?')
        if self.clear_prompt:
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.region_entry.delete(0, tk.END)
            self.isp_entry.delete(0, tk.END)
            self.model_entry.delete(0, tk.END)
            self.pop_entry.delete(0, tk.END)
            self.dop_entry.delete(0, tk.END)
            self.issue_entry.delete(0, tk.END)
            self.wf_entry.delete(0, tk.END)
            self.ts_entry.delete(1.0, tk.END)
            self.notes_entry.delete(1.0, tk.END)
            messagebox.showinfo(title='Cleared!', message='Information cleared.')

    def settings(self):
        if not os.path.exists(self.set_dir):
            os.makedirs(self.set_dir)
        elif not os.path.exists(self.f_dir):
            open(self.f_dir, 'x')
        messagebox.showinfo(title='Select directory', message='Please select the directory where you want to save.')
        self.note_dir = filedialog.askdirectory()
        with open(self.f_dir, 'w') as file:
            file.write(self.note_dir)

    def save_info(self):
        if not os.path.exists(self.f_dir):
            messagebox.showerror(title='Directory not found', message='Please set-up your preferred directory to save.')
        else:
            with open(self.f_dir, 'r') as file:
                self.contents = file.read()
            if self.contents == '' or not os.path.exists(self.contents):
                messagebox.showerror(title='Directory not found',
                                     message='Please set-up properly your preferred directory to save.')
            else:
                self.save_prompt = messagebox.askyesno(title='Current directory', message='Your current save directory is {}. Go to '
                                                                       'Settings if you want to change. Proceed?'.format(self.contents))
                if self.save_prompt:
                    self.f_date = datetime.now().strftime('%Y-%m-%d')
                    self.note_file = '{}.txt'.format(self.f_date)
                    self.callnote = self.contents + self.note_file
                    with open(self.callnote, 'a') as file:
                        file.write(self.get_val() + '\n++++++++++++++++++++++++++++++\n')


if __name__ == '__main__':
    root = tk.Tk()
    mainWin(root)
    root.mainloop()