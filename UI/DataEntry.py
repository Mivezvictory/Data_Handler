import tkinter as tk     
from UI import StartPage
from UI import DataApp
from UI import MetaHandler_Sample


class DataEntry:
    SCREENS = (StartPage.StartPage, DataApp.DataApp, MetaHandler_Sample.MetaHandler_Sample)

    MINIMUM_HEIGHT = 650
    MINIMUM_WIDTH = 1200

    def __init__(self, parent):
        """This Screen will be used to allow switching between screens.
            Other screens will be placed within its frame."""
        self.parent = parent
        #height = 650
        #width = 1200
        self.parent.minsize(DataEntry.MINIMUM_WIDTH, DataEntry.MINIMUM_HEIGHT)

        self.my_container_frame = tk.Frame(parent, bg="red")
        self.my_container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.my_container_frame.grid_rowconfigure(0, weight=1)
        self.my_container_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create a menu bar at the top.
        menu_bar = tk.Menu(self.my_container_frame)
        file = tk.Menu(menu_bar, tearoff=0)
        file.add_command(label='New window')
        file.add_command(label='Open')
        file.add_command(label='Save')
        file.add_command(label='Save As...')
        file.add_command(label='Exit')
        menu_bar.add_cascade(label='File', menu=file)

        """Loop through all the screens provided,
           Make an instance of each screen,
           Make a dictionary with all their names as keys and frame objects as values
           Set their position on the grid."""
        for current_screen in self.SCREENS:
            page_name = current_screen.__name__
            frame = current_screen(parent=self.my_container_frame, controller=self)
            self.frames[page_name] = frame
            frame.my_frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page by default.
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Given the name of a screen it will show that screen."""
        frame = self.frames[page_name]
        frame.my_frame.tkraise()
