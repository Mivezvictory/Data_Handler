import Tkinter as tk
from Tkinter import *
#from UI.DataTemplates import Template_1, Template_2
import pandas as pd
from pandas import DataFrame

from tkFileDialog import askopenfilename
import tkFileDialog
import os
import tkMessageBox


class TemplateDataProcessor:
    template_1_labels = ["Station", "ChemID", "Bottle#", "Date", "Latitude", "Longitude", "Arrival time", "Departure",
                        "Depth(m)", "Lowe depth(m)", "Lowe temp(c)", "Analyst Name", "Flurometer depth(m)", "Time on",
                         "Time off", "Serial No.", "Secchi Depth", "Air temperature", "Surface temperature", "Surface sample time",
                        "Bottle temperature", "Bottle sample depth", "Bottom bottle ID", "Phytoplankton sample",
                        "Zooplankton depth(m)", "Formalin added", "Vodka added", "Wave Ht(m)", "CBM sample"]

    template_2_labels = ["Station", "ChemID", "Bottle#", "Date", "Latitude", "Longitude", "Arrival time", "Departure",
                         "Depth(m)", "Lowe depth(m)", "Lowe temp(c)", "Analyst Name", "Flurometer depth(m)", "Time on",
                         "Time off", "Serial No.", "Secchi Depth", "Air temperature", "Surface temperature",
                         "Surface sample time",
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
        for i in range(0, len(TemplateDataProcessor.template_1_labels)):
            new_list[TemplateDataProcessor.template_1_labels[i]] = options[TemplateDataProcessor.template_1_labels[i]]
        df = pd.DataFrame(new_list, index=[0])

        df = df[TemplateDataProcessor.template_1_labels]  # Re-orders the column of the csv file to match the template labels
        df.to_csv(file_name, index=None, header=True)

    def compare_csv_file(self, csv_file):
        new_dict = {}
        column_list = csv_file.columns.values
        if len(column_list) == len(TemplateDataProcessor.template_1_labels):
            for i in range(0, len(TemplateDataProcessor.template_1_labels)):
                if column_list[i] != TemplateDataProcessor.template_1_labels[i]:
                    return False
        else:
            return False

        return True

    def read_file(self, csv_file):
        new_dict = {}
        value = self.compare_csv_file(csv_file)
        if value:
            for i in range(0, len(TemplateDataProcessor.template_1_labels)):
                new_dict[TemplateDataProcessor.template_1_labels[i]] = csv_file.iloc[0][TemplateDataProcessor.template_1_labels[i]]
        else:
            return False

        return new_dict

    def handle_clearing_template(self, widget_list):
        for key in widget_list:
            if isinstance(widget_list[key], Text):
                widget_list[key].delete(1.0, END)
            else:
                widget_list[key].delete(0, END)





