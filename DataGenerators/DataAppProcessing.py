import Tkinter as tk
from Tkinter import *
#from UI import DataApp
import pandas as pd
from pandas import DataFrame


class DataAppProcessing:
    template_labels = ["Station", "ChemID", "Bottle#", "Date", "Latitude", "Longitude", "Arrival time", "Departure",
                        "Depth(m)", "Lowe depth(m)", "Lowe temp(c)", "Analyst Name", "Flurometer depth(m)", "Time on",
                         "Time off", "Serial No.", "Secchi Depth", "Air temperature", "Surface temperature", "Surface sample time",
                        "Bottle temperature", "Bottle sample depth", "Bottom bottle ID", "Phytoplankton sample",
                        "Zooplankton depth(m)", "Formalin added", "Vodka added", "Wave Ht(m)", "CBM sample"]

    def get_widget_entry(self, widget):
        if isinstance(widget, Text):
            return widget.get("1.0", "end-1c")
        return widget.get()

    # Accepts 2 parameters, a dictionary and the name of a file
    # This function takes a dictionary containing key value pairs and creates a csv file with the provided file name
    # Also writes the csv file to the location/dir passed along with the file name
    def create_csv_file(self, options, file_name):
        new_list = {}
        for i in range(0, len(DataAppProcessing.template_labels)):
            new_list[DataAppProcessing.template_labels[i]] = options[DataAppProcessing.template_labels[i]]
        df = pd.DataFrame(new_list, index=[0])

        df = df[DataAppProcessing.template_labels]  # Re-orders the column of the csv file to match the template labels
        df.to_csv(file_name, index=None, header=True)

