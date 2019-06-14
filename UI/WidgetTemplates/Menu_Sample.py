import Tkinter
from tkFileDialog import askopenfilename
import Tkinter, Tkconstants, tkFileDialog
from UI import DataApp
import os
import tkMessageBox
import pandas as pd


"""We generally need to build grids so it we'll have a function for that"""


class Menu_Sample:
    def __init__(self, master):
        # Master GUI handler
        self.master = master
       # self.controller = controller
        # A frame is an invisible box that we put stuff into. In this case it belongs to self.maste
        self.file_name = ''
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

        file_menu.add_command(label='New window', command=self.new_window)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save As...', command=self.save_file_as)
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

    def new_window(self):
        execfile('app.py')

    def open_file(self):
        if os.name == 'nt':
            opened_file_path = askopenfilename(initialdir="C:\\", title="Select file",
                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        else:
            opened_file_path = askopenfilename(initialdir="/", title="Select file",
                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            #TODO: upon opening a file, first check the file to see if it is a format we can open, before opening it

        if opened_file_path:
            #TODO: make sure only csv files are being passed so as to no have some mad error you cant check for
            opened_file_csv = pd.read_csv(opened_file_path)
            if DataApp.DataApp.handle_loading_template(opened_file_csv) == False:
                tkMessageBox.showinfo("Title", "please load correct file")



    def save_file(self):
        if self.file_name:  # ensures the save as procedure is only executed if a file name is entered and saved.

            try:
                f = open(self.file_name, "w+")
                DataApp.DataApp.handle_forward_button(self.file_name)
                f.close()
            except IOError:  # files cannot be saved to while they are open on users device
                tkMessageBox.showinfo("Title", "please close file before saving new changes")
                # inform users to close file they are trying to save to, if file is currently opened
        else:  # if current changes have not been saved to the device, open the dialogue and get the user to save file
            self.save_file_as()

    def save_file_as(self):
        #  opens a dialogue to get the name and file type from the user
        self.file_name = tkFileDialog.asksaveasfilename(initialdir="C:\\", title="Select file",
                                                        filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

        if self.file_name:  # ensures the save as procedure is only executed if a file name is entered and saved.
            DataApp.DataApp.handle_forward_button(self.file_name)
            tkMessageBox.showinfo("Title", "File saved")

    def client_exit(self):
        exit()

    def make_json(self):
        print("I will be used to make a json file for the metadata...")
        return

    def make_csv(self):
        print("I will be used to make a csv file for the metadata...")
        return
