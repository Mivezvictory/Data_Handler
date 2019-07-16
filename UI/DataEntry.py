import Tkinter as tk
from UI import StartPage
from UI.DataTemplates import Template_1, Template_2, Template_3
from UI import MetaHandler_Sample
from UI.WidgetTemplates import Menu_Sample


class DataEntry:
    SCREENS = (StartPage.StartPage, Template_1.DataApp, MetaHandler_Sample.MetaHandler_Sample, Template_2.CustomPage,
               Template_3.Template_3)

    MINIMUM_HEIGHT = 650
    MINIMUM_WIDTH = 1200
    my_frames = {}

    def __init__(self, parent):
        """This Screen will be used to allow switching between screens.
            Other screens will be placed within its frame."""
        self.parent = parent
        self.parent.minsize(DataEntry.MINIMUM_WIDTH, DataEntry.MINIMUM_HEIGHT)

        self.my_container_frame = tk.Frame(parent)
        self.my_container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.my_container_frame.grid_rowconfigure(0, weight=1)
        self.my_container_frame.grid_columnconfigure(0, weight=1)



        """Loop through all the screens provided,
           Make an instance of each screen,
           Make a dictionary with all their names as keys and frame objects as values
           Set their position on the grid."""

        for current_screen in self.SCREENS:
            page_name = current_screen.__name__
            frame = current_screen(parent=self.my_container_frame, controller=self, my_frames=DataEntry.my_frames)
            DataEntry.my_frames[page_name] = frame
            frame.my_frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page by default.
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Given the name of a screen it will show that screen."""
        frame = self.my_frames[page_name]
        frame.my_frame.tkraise()
        self.toolMenu = Menu_Sample.Menu_Sample(self.parent, page_name, DataEntry.my_frames)
        self.toolMenu.build_menu()

