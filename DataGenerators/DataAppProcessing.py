import Tkinter as tk
from Tkinter import *
#from UI import DataApp
from pandas import DataFrame


class DataAppProcessing:
    template_labels = ["Station", "ChemID", "Bottle#", "Date", "Latitude", "Longitude", "Arrival time", "Departure",
         "Depth(m)", "Lowe depth(m)", "Lowe temp(c)", "Analyst Name", "Flurometer depth(m)", "Time on",
         "Time off", "Serial No.", "Secchi Depth", "Air temperature", "Surface temperature", "Surface sample time",
         "Bottle temperature", "Bottle sample depth", "Bottom bottle ID", "Phytoplankton sample",
         "Zooplankton depth(m)",
         "Formalin added", "Vodka added", "Wave Ht(m)", "CBM sample"
         ]


    def get_widget_entry(self, widget):
        if isinstance(widget, Text):
            return widget.get("1.0", "end-1c")
        return widget.get()

    def create_csv_file(self, options, file_name):
        newlist = {}
        print options['Station']
        print options
        for i in range(0, len(DataAppProcessing.template_labels)):
            newlist[DataAppProcessing.template_labels[i]] = options[DataAppProcessing.template_labels[i]]
        df = DataFrame(newlist, index=[0])
        #print df
        print newlist
        df.to_csv(file_name, index=None, header=True)
        return df
