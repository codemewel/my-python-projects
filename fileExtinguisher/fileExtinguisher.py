import os, filetype, re
import tkinter as tk
from tkinter import filedialog, messagebox


class fileWindow:
    def __init__(self, filetype, directory):
        self.filetype = filetype
        self.filedir = directory
        self.f_window = tk.Toplevel()
        self.f_window.title('Files found!')
        self.f_window.minsize(300,150)
        self.f_window.resizable(0,0)
        self.y_scroll = tk.Scrollbar(self.f_window)
        self.y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.f_txt = tk.Label(self.f_window, text='Select filetype')
        self.f_txt.pack(padx=5, pady=5)
        self.ftype_list = tk.Listbox(self.f_window, selectmode=tk.SINGLE, yscrollcommand=self.y_scroll.set)
        self.ftype_list.pack(pady=10, padx=10, expand=tk.YES, fill=tk.BOTH)
        for self.filetype_item in self.filetype:
            self.ftype_list.insert(tk.END, self.filetype_item + ': {} files'.format(self.filetype[self.filetype_item]))
        self.y_scroll.config(command=self.ftype_list.yview)
        self.ex_btn = tk.Button(self.f_window, text='EXTINGUISH', command=self.extinguish_file)
        self.ex_btn.pack(pady=5)

    def extinguish_file(self):
        self.ext_selection = self.ftype_list.get(self.ftype_list.curselection())
        self.ext = re.search(r'.*:', self.ext_selection)
        self.extension = '.' + self.ext.group().strip(':')
        self.query = messagebox.askquestion(
            title='WARNING!', message='This will permanently delete all {} files in {}, Continue?'.format(
                self.extension, self.filedir), parent=self.f_window)
        if self.query == 'yes':
            for self.filename in os.listdir(self.filedir):
                if self.filename.endswith(self.extension):
                    self.file_path = os.path.join(self.filedir, self.filename)
                    os.remove(self.file_path)
            messagebox.showinfo(message='All {} files EXTINGUISHED!'.format(self.extension), parent=self.f_window)
            self.f_window.destroy()


class mainWindow:
    def __init__(self, base):
        self.base = base
        self.base.title('File Extinguisher')
        self.base.geometry('300x150+20+20')
        self.base.resizable(0,0)
        self.main_frame = tk.Frame(self.base)
        self.main_frame.pack()
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.title_frame = tk.Label(self.main_frame, text='Extinguish Files Easily!', foreground='red')
        self.title_frame.grid(column=0, row=0, columnspan=2, pady=(20, 5))
        self.title_frame.configure(font=('Roboto Condensed', 15, 'bold'))
        self.dir_btn = tk.Button(self.main_frame, text='Select Directory', command=self.get_dir)
        self.dir_btn.grid(column=0, row=1, columnspan=2)
        self.txt = tk.Label(self.main_frame, text='by code me Wel')
        self.txt.grid(column=0, row=2, columnspan=2, pady=5)

    def get_dir(self):
        self.f_dir = filedialog.askdirectory()
        self.f_dic = {}
        self.f_list = []
        self.i_num = 1
        for self.file in os.listdir(self.f_dir):
            self.f_path = self.f_dir + '/' + self.file
            self.isfile = os.path.isfile(self.f_path)
            if self.isfile:
                self.f_type = filetype.guess(self.f_path)
                if self.f_type is None:
                    self.f_ext = os.path.splitext(self.f_path)[1]
                    self.f_list.append(self.f_ext.strip('.'))
                else:
                    self.f_ext = self.f_type.extension
                    self.f_list.append(self.f_ext)
        for self.item in self.f_list:
            if self.item in self.f_dic:
                self.f_dic[self.item] += self.i_num
            else:
                self.f_dic[self.item] = self.i_num
        if not self.f_dic:
            messagebox.showinfo(title='OOppss!', message='No files found in {} directory!'.format(self.f_dir))
        else:
            fileWindow(self.f_dic, self.f_dir)


if __name__ == '__main__':
    root = tk.Tk()
    mainWindow(root)
    root.mainloop()