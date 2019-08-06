import Tkinter as tk
from Tkinter import *
from pandas import DataFrame
from DataGenerators import TemplateDataProcessor
from UI.WidgetTemplates import Menu_Sample


# TODO: rename template to match with other templates once constructed
# TODO: give each template a unique ID, for identification when opening files


class Template_4:
    # class variables for building UI labels and entry boxes
    label_width = 0.15
    label_height = 0.0325
    entry_width = 0.07
    entry_height = 0.03

    # class variables for UI layout
    entry_boldness = 2
    label_font = ("", 12)
    label_color = "white"
    entry_color = "white"
    template_identifier = "Template_3"
    template_number = 2

    # list of all widgets created on each page
    # helps with collecting information from each UI. And easy use of loop to get all widget entries
    widget_list = {}

    def __init__(self, parent, controller, my_frames):
        self.master = parent
        self.my_controller = controller
        self.my_frame = tk.Frame(self.master, bg='#ffffff')  # creates a frame for this UI
        self.my_frame.place(relwidth=1, relheight=1)
        self.data_processor = TemplateDataProcessor.TemplateDataProcessor()

        #self.build_template()  # builds the template
