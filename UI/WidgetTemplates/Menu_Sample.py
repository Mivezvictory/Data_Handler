import tkinter

"""We generally need to build grids so it we'll have a function for that"""


class Menu_Sample:
    def __init__(self, master):
        # Master GUI handler
        self.master = master
        # A frame is an invisible box that we put stuff into. In this case it belongs to self.master
        self.build_toolmenu()

    def build_toolmenu(self):
        # Create a menu object for the top of the window
        menu = tkinter.Menu(self.master)
        (self.master).config(menu=menu)

        # Add a drop-down menu for the File option
        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Export as Json", command = self.make_json)
        file_menu.add_command(label="Export into Csv", command = self.make_csv)
        menu.add_cascade(label="File", menu=file_menu)
        return

    def make_json(self):
        print("I will be used to make a json file for the metadata...")
        return

    def make_csv(self):
        print("I will be used to make a csv file for the metadata...")
        return
