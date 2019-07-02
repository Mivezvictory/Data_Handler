from tkFileDialog import askopenfilename
import tkinter
import tkFileDialog
import os
import traceback
import pandas as pd
import tkMessageBox
"""We generally need to build grids so it we'll have a function for that"""


class Menu_Sample:
    def __init__(self, master, page_identifier, template_list):
        # Master GUI handler
        self.master = master
        self.page_identifier = page_identifier  # name of current active page, gotten from DataEntry class
        self.template_list = template_list  # A list of instances of all pages created on the Application
        self.file_name = ''  # Name of current file in use by the Application

    def build_menu(self):
        menu = tkinter.Menu(self.master)
        self.master.config(menu=menu)
        if self.page_identifier != "StartPage":  # menu is not built for the start page
            self.build_file_menu(menu)
            self.build_edit_menu(menu)
            self.build_help_menu(menu)

    def build_file_menu(self, menu):
        # Create a menu object for the top of the window

        # Add a drop-down menu for the File option
        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_cascade(label="Save", command=self.save_file)
        file_menu.add_cascade(label="Save As...", command=self.save_file_as)
        file_menu.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file_menu)
        return

    def build_edit_menu(self, menu):
        edit = tkinter.Menu(menu)

        edit.add_command(label='Clear template', command=self.clear_template)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

    def build_help_menu(self, menu):
        help = tkinter.Menu(menu)

        help.add_command(label='Help', command=self.clear_template)
        menu.add_cascade(label='Help', menu=help)

    """
    This method calls the current active template and clears each entry box
    0 arguments
    calls the template class method "handle_clearing_template"
    """
    def clear_template(self):
        try:

            curr_template = self.template_list[self.page_identifier]
            curr_template.handle_clearing_template()
        except AttributeError:
            traceback.print_exc()

    """
    This method opens a csv file already saved on users computer and files the entry boxes on the Applications templates
    with the appropriate entries
    0 arguments
    calls the template class method "open_saved_files"
    upon opening a file not suited to the current template screen, an error message box is shown to the user
    """
    def open_file(self):
        if os.name == 'nt':
            opened_file_path = askopenfilename(initialdir="C:\\", title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        else:
            opened_file_path = askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

        if opened_file_path:
            # TODO: make sure only csv files are being passed so as to no have some mad error you cant check for
            opened_file_csv = pd.read_csv(opened_file_path)
            try:

                curr_template = self.template_list[self.page_identifier]
                if curr_template.open_saved_files(opened_file_csv) == False:
                    # TODO: have a better message box message for christ sake
                    tkMessageBox.showinfo("Title", "please load correct file")

            except AttributeError:
                traceback.print_exc()

    """
       This method saves a templates entries as a csv file in the appropriate order
       0 arguments
       calls the template class method "save_data_entries"
    """
    def save_file(self):
        if self.file_name:  # ensures the save as procedure is only executed if a file name is entered and saved.
            try:
                f = open(self.file_name, "w+")
                try:

                    curr_template = self.template_list[self.page_identifier]
                    curr_template.save_data_entries(self.file_name)
                except AttributeError:
                    traceback.print_exc()

                f.close()
            except IOError:  # files cannot be saved to while they are open on users device
                tkMessageBox.showinfo("Title", "please close file before saving new changes")
                # inform users to close file they are trying to save to, if file is currently opened
        else:  # if current changes have not been saved to the device, open the dialogue and get the user to save file
            self.save_file_as()

    """
         This method saves a templates entries as a csv file in the appropriate order
         0 arguments
         calls the template class method "save_data_entries"
      """
    def save_file_as(self):
        #  opens a dialogue to get the name and file type from the user
        self.file_name = tkFileDialog.asksaveasfilename(initialdir="C:\\", title="Select file",
                                                        filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

        if self.file_name:  # ensures the save as procedure is only executed if a file name is entered and saved.
            try:

                curr_template = self.template_list[self.page_identifier]
                curr_template.save_data_entries(self.file_name)
            except AttributeError:
                traceback.print_exc()

            tkMessageBox.showinfo("Title", "File saved")

    def client_exit(self):
        exit()
