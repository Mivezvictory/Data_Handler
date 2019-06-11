import Tkinter
from tkFileDialog import askopenfilename
import os
"""We generally need to build grids so it we'll have a function for that"""


class Menu_Sample:
    def __init__(self, master):
        # Master GUI handler
        self.master = master
        # A frame is an invisible box that we put stuff into. In this case it belongs to self.maste
        self.build_menu()

    def build_menu(self):
        menu = Tkinter.Menu(self.master)
        self.master.config(menu=menu)

        self.build_file_menu(menu)
        self.build_edit_menu(menu)
        self.build_insert_menu(menu)
        self.build_help_menu(menu)

        return

    def build_file_menu(self, menu):
        file_menu = Tkinter.Menu(menu)

        file_menu.add_command(label='New window', command='__main__')
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save')
        file_menu.add_command(label='Save As...')
        file_menu.add_command(label="Export as Json", command=self.make_json)
        file_menu.add_command(label="Export into Csv", command=self.make_csv)

        file_menu.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label="File", menu=file_menu)
        return

    def build_edit_menu(self, menu):
        edit = Tkinter.Menu(menu)

        edit.add_command(label='Undo')
        edit.add_command(label='redo')
        edit.add_command(label='find')
        edit.add_command(label='find & replace')
        menu.add_cascade(label='Edit', menu=edit)

    def build_insert_menu(self, menu):
        insert = Tkinter.Menu(menu)

        insert.add_command(label='Text box')
        menu.add_cascade(label='Insert', menu=insert)

    def build_help_menu(self, menu):
        help = Tkinter.Menu(menu)

        help.add_command(label='Help')
        menu.add_cascade(label='Help', menu=help)

    def open_file(self):
        if os.name == 'nt':
            opened_file = askopenfilename(initialdir="C:\\", title="Select file",
                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        else:
            opened_file = askopenfilename(initialdir="/", title="Select file",
                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            #TODO: upon opening a file, first check the file to see if it is a format we can open, before opening it
        #print opened_file
        return


    def client_exit(self):
        exit()

    def make_json(self):
        print("I will be used to make a json file for the metadata...")
        return

    def make_csv(self):
        print("I will be used to make a csv file for the metadata...")
        return
