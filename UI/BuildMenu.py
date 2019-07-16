import Tkinter as tk
from Tkinter import *


class BuildMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.build_menu()

    def build_menu(self):
        menu = Menu(self.parent)

        #self.parent.config(menu=menu)
        print " we got here"
        self.build_file_menu(menu)
        self.build_edit_menu(menu)
        self.build_insert_menu(menu)
        self.build_help_menu(menu)
        self.parent.config(menu=menu)
        # first line of entries

    def build_file_menu(self, menu):
        file = Menu(menu, tearoff=0)

        file.add_command(label='New window', command='__main__')
        file.add_command(label='Open')
        file.add_command(label='Save')
        file.add_command(label='Save As...')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

    def build_edit_menu(self, menu):
        edit = Menu(menu, tearoff=0)

        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

    def build_insert_menu(self, menu):
        insert = Menu(menu, tearoff=0)

        insert.add_command(label='Text box')
        menu.add_cascade(label='Insert', menu=insert)

    def build_help_menu(self, menu):
        help = Menu(menu, tearoff=0)

        help.add_command(label='Help')
        menu.add_cascade(label='Help', menu=help)

    def client_exit(self):
        exit()