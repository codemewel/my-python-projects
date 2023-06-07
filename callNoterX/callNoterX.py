import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class mainWin:
    def __init__(self, base):
        self.base = base
        self.base.title('callNoter X')
        self.base.minsize(400,500)
        self.base.resizable(0,0)
        self.main_frame = tk.Frame(self.base)
        self.main_frame.pack()
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
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
        self.cx_label.grid(column=0, row=0, padx=10, pady=(10, 5), ipady=5, ipadx=5)
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
        self.sop_label.grid(column=0, row=2, ipady=5, ipadx=10)
        self.issue_label = tk.Label(self.sop_label, text='Issue:')
        self.issue_label.grid(column=0, row=0)
        self.issue_entry = tk.Entry(self.sop_label, textvariable=self.confirm_issue)
        self.issue_entry.grid(column=1, row=0, sticky='w')
        self.wf_label = tk.Label(self.sop_label, text='Workflow:')
        self.wf_label.grid(column=2, row=0)
        self.wf_entry = tk.Entry(self.sop_label, width=10, textvariable=self.confirm_wf)
        self.wf_entry.grid(column=3, row=0, sticky='w')
        self.ts_label = tk.Label(self.sop_label, text='Troubleshooting:')
        self.ts_label.grid(column=0, row=1, columnspan=2, sticky='w', pady=(5,1))
        self.ts_entry = ScrolledText(self.sop_label, height=10, width=50)
        self.ts_entry.grid(column=0, row=2, columnspan=4)
        self.ts_entry.bind('<Control-a>', self.select_all)
        self.copy_btn = tk.Button(self.main_frame, text='Copy All', command=self.copy_all)
        self.copy_btn.grid(column=0, row=3, sticky='ew', padx=10, pady=5)
        self.notes_label = tk.LabelFrame(self.main_frame, text='Additional Info')
        self.notes_label.grid(column=0, row=5, ipady=5, ipadx=10)
        self.notes_entry = ScrolledText(self.notes_label, height=5, width=50)
        self.notes_entry.grid(column=0, row=0, columnspan=4)
        self.save_btn = tk.Button(self.main_frame, text='Save')
        self.save_btn.grid(column=0, row=6, sticky='w', padx=10)
        self.clear_btn = tk.Button(self.main_frame, text='Clear')
        self.clear_btn.grid(column=0, row=7, sticky='w', padx=10)
        self.author = tk.Label(self.main_frame, text='Powered by code Me Wel')
        self.author.grid(column=0, row=8, pady=(15,5))

    def select_all(self, event):
        self.event = event
        self.event.widget.tag_add('sel', '1.0', 'end')
        return 'break'

    def copy_all(self, *args):
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
        self.all_info = '' \
                        'Name: {}\nPhone: {}\nEmail: {}\nRegion: {}\nISP: {}\nModel: {}' \
                        '\nPOP: {}\nDOP: {}\nIssue: {}\nWorkflow: {}\nTS:\n{}'.format(
            self.name_var, self.phone_var, self.email_var, self.region_var, self.isp_var, self.model_var,
        self.pop_var, self.dop_var, self.issue_var, self.wf_var, self.ts_var)
        print(self.all_info)


if __name__ == '__main__':
    root = tk.Tk()
    mainWin(root)
    root.mainloop()