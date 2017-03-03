from Tkinter import *
import tkMessageBox
import tkFileDialog


class Text_editor():
    "docstring for Text_editor"

    def __init__(self):
        self.CreatUI()
        mainloop()

    def CreatUI(self):
        self.tk = Tk()
        menubar = Menu(self.tk)
        # add a new menu "file" ,including open\save\new file\
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(lable='open', command=self.open)
        file_menu.add_command(label='new file', command=self.new_file)
        file_menu.add_command(label='save', command=self.save)
        menubar.add_cascade(label='File', menu=file_menu)

        # add another menu"edit",including copy\cut\paste\highlight
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label='copy', command=self.copy)
        edit_menu.add_command(label='cut', command=self.cut)
        edit_menu.add_command(label='paste', command=self.paste)
        edit_menu.add_command(label='highlight', command=self.highlight)
        menubar.add_cascade(label='Edit', menu=edit_menu)

        self.tk.config(menu=menubar)
        self.text = Text()
        self.text.pack()

    def open():
        global filename
        systype = platform.system()
        if systype == 'windows':
            basedir = 'c:\\'
        else:
            basedir = '/'
        filename = tkFileDialog.askopenfilename(initialdir=basedir)


text_editor = Text_editor()
