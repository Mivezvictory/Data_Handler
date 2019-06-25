from tkFileDialog import askopenfilename
import tkinter, tkFileDialog
from DataGenerators import TemplateDataProcessor
#from UI.DataTemplates import Template_1
import tkMessageBox
"""We generally need to build grids so it we'll have a function for that"""


class Menu_Sample:
    def __init__(self, master, template_list, page_identifier):
        # Master GUI handler
        self.master = master
        self.page_identifier = page_identifier
        self.template_list = template_list
        self.data_processor = TemplateDataProcessor.TemplateDataProcessor()
        # A frame is an invisible box that we put stuff into. In this case it belongs to self.master
        self.file_name = ''

    def build_menu(self):
        menu = tkinter.Menu(self.master)
        self.master.config(menu=menu)
        if self.page_identifier != "StartPage":
            self.build_file_menu(menu)
            self.build_edit_menu(menu)

    def build_file_menu(self, menu):
        # Create a menu object for the top of the window

        # Add a drop-down menu for the File option
        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Open", command=self.make_json)
        file_menu.add_cascade(label="Save")
        file_menu.add_command(label="Export as Json", command=self.make_json)
        file_menu.add_command(label="Export into Csv", command=self.make_csv)
        file_menu.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file_menu)
        return

    def build_edit_menu(self, menu):
        edit = tkinter.Menu(menu)

        edit.add_command(label='Clear template', command=self.clear_template)
        edit.add_command(label='Undo')
        edit.add_command(label='redo')
        edit.add_command(label='find')
        edit.add_command(label='find & replace')
        menu.add_cascade(label='Edit', menu=edit)

    def clear_template(self):
        self.data_processor.handle_clearing_template(self.page_identifier)

    def open_file(self):
        self.data_processor.handle_save_option(self.page_identifier)

    def make_json(self):
        #if self.page_identifier == 0:
        print("I will be used to make a json file for the metadata...")
        return

    def make_csv(self):
        print("I will be used to make a csv file for the metadata...")
        return

    def client_exit(self):
        exit()

    def open_file(self):
        if os.name == 'nt':
            opened_file_path = askopenfilename(initialdir="C:\\", title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        else:
            opened_file_path = askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            # TODO: upon opening a file, first check the file to see if it is a format we can open, before opening it

        if opened_file_path:
            # TODO: make sure only csv files are being passed so as to no have some mad error you cant check for
            opened_file_csv = pd.read_csv(opened_file_path)
            if Template_1.DataApp.handle_loading_template(opened_file_csv) == False:
                # TODO: have a better message box message for christ sake
                tkMessageBox.showinfo("Title", "please load correct file")
