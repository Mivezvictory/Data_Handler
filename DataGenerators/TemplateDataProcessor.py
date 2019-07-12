import Tkinter as tk
from Tkinter import *
#from UI.DataTemplates import Template_1, Template_2
import pandas as pd
import xlsxwriter
from pandas import DataFrame

from tkFileDialog import askopenfilename
import tkFileDialog
import os
import tkMessageBox


class TemplateDataProcessor:

    template_labels =[
                        ["Station", "Bottle#", "Date", "Latitude", "Longitude", "Arrival time", "Departure",
                        "Depth(m)", "Lowe depth(m)", "Lowe temp(c)", "Analyst Name", "Flurometer depth(m)", "Time on",
                         "Time off", "Serial No.", "#Casts", "Secchi Depth", "Air temperature", "Surface temperature", "Surface sample time",
                        "Bottle temperature", "Bottle sample depth", "Bottom bottle ID", "Phytoplankton Sample",
                        "Zooplankton depth(m)", "Formalin added", "Wave Ht(m)", "CBM sample", "Weather Conditions",
                         "Beaufort Wind Scale"],

                        ["Station", "ChemID", "Bottle#", "Date", "Latitude", "Longitude", "Arrival time", "Departure",
                         "Depth(m)", "Lowe depth(m)", "Lowe temp(c)", "Analyst Name", "Flurometer depth(m)", "Time on",
                         "Time off", "Serial No.", "Secchi Depth", "Air temperature", "Surface temperature",
                         "Surface sample time",
                         "Bottle temperature", "Bottle sample depth", "Bottom bottle ID", "Phytoplankton sample",
                         "Zooplankton depth(m)", "Formalin added", "Vodka added", "Wave Ht(m)", "CBM sample"],

                        ["Station", "Date", "Latitude", "Longitude", "Arrival time", "Departure time", "Bottle ID",
                         "Surface Sample Time", "Air Temperature", "Surface Temperature",
                         "Time On", "Time Off", "Serial No.",
                         "CTD Depth(m)", "Phytoplankton Sample", "CBM Sample", "Weather Conditions", "Beaufort Wind Scale", "Notes"],

                        ["Station", "Date", "Latitude", "Longitude", "Arrival time", "Position1", "DTW1", "DOW1_1",
                         "DOW1_2", "DOW1_3", "Directions1", "WOW1", "Position2", "DTW2", "DOW2_1",
                         "DOW2_2", "DOW2_3", "Directions2", "WOW2", "Position3", "DTW3", "DOW3_1",
                         "DOW3_2", "DOW3_3", "Directions3", "WOW3", "Notes"],

                        ["Station", "Date", "Latitude", "Longitude", "Arrival time", "Length of flow measurement1",
                         "Position1_1", "time1_1_1", "time1_1_2", "time1_1_3",
                         "Position1_2", "time1_2_1", "time1_2_2", "time1_2_3",
                         "Position1_3", "time1_3_1", "time1_3_2", "time1_3_3", "Length of flow measurement2",
                         "Position2_1", "time2_1_1", "time2_1_2", "time2_1_3",
                         "Position2_2", "time2_2_1", "time2_2_2", "time2_2_3",
                         "Position2_3", "time2_3_1", "time2_3_2", "time2_3_3", "Length of flow measurement3",
                         "Position3_1", "time3_1_1", "time3_1_2", "time3_1_3",
                         "Position3_2", "time3_2_1", "time3_2_2", "time3_2_3",
                         "Position3_3", "time3_3_1", "time3_3_2", "time3_3_3", "Notes"],

                        ["Station", "Date", "Latitude", "Longitude", "Arrival time", "Departure time", "Bottle ID",
                         "Surface Sample Time", "Air Temperature", "Surface Temperature",
                         "Time On", "Time Off", "Serial No.",
                         "CTD Depth(m)", "Phytoplankton Sample", "CBM Sample", "Weather Conditions", "Beaufort Wind Scale",
                         "Position1", "DTW1", "DOW1_1",
                         "DOW1_2", "DOW1_3", "Directions1", "WOW1", "Position2", "DTW2", "DOW2_1",
                         "DOW2_2", "DOW2_3", "Directions2", "WOW2", "Position3", "DTW3", "DOW3_1",
                         "DOW3_2", "DOW3_3", "Directions3", "WOW3", "Length of flow measurement1",
                         "Position1_1", "time1_1_1", "time1_1_2", "time1_1_3",
                         "Position1_2", "time1_2_1", "time1_2_2", "time1_2_3",
                         "Position1_3", "time1_3_1", "time1_3_2", "time1_3_3", "Length of flow measurement2",
                         "Position2_1", "time2_1_1", "time2_1_2", "time2_1_3",
                         "Position2_2", "time2_2_1", "time2_2_2", "time2_2_3",
                         "Position2_3", "time2_3_1", "time2_3_2", "time2_3_3", "Length of flow measurement3",
                         "Position3_1", "time3_1_1", "time3_1_2", "time3_1_3",
                         "Position3_2", "time3_2_1", "time3_2_2", "time3_2_3",
                         "Position3_3", "time3_3_1", "time3_3_2", "time3_3_3", "Notes"]


                    ]

    def get_widget_entry(self, widget):
        if isinstance(widget, Text):
            return widget.get("1.0", "end-1c")
        else:
            return widget.get()

    # Accepts 2 parameters, a dictionary and the name of a file
    # This function takes a dictionary containing key value pairs and creates a csv file with the provided file name
    # Also writes the csv file to the location/dir passed along with the file name
    def create_csv_file(self, options, file_name, template_num):
        new_list = {}
        for i in range(0, len(TemplateDataProcessor.template_labels[template_num])):
            new_list[TemplateDataProcessor.template_labels[template_num][i]] = options[TemplateDataProcessor.template_labels[template_num][i]]
        df = pd.DataFrame(new_list, index=[0])
        df = df[TemplateDataProcessor.template_labels[template_num]]  # Re-orders the column of the csv file to match the template labels
        df.to_csv(file_name, index=None, header=True)

    def make_header_format(self, file_name):
        file_names = file_name.split()
        xlsx = file_names[0] + "xlsx"


    """
    Compares the entry labels present in a file to the labels in a list to ensure the file being opened has all the 
    required labels
    accepts 1 parameter: the csv file being opened 
    """
    def compare_csv_file(self, csv_file, template_num):
        new_dict = {}
        column_list = csv_file.columns.values
        if len(column_list) == len(TemplateDataProcessor.template_labels[template_num]):
            for i in range(0, len(TemplateDataProcessor.template_labels[template_num])):
                if column_list[i] != TemplateDataProcessor.template_labels[template_num][i]:
                    return False
        else:
            return False

        return True

    def read_file(self, csv_file, template_num):
        new_dict = {}
        value = self.compare_csv_file(csv_file, template_num)
        if value:
            for i in range(0, len(TemplateDataProcessor.template_labels[template_num])):
                new_dict[TemplateDataProcessor.template_labels[template_num][i]] = csv_file.iloc[0][TemplateDataProcessor.template_labels[template_num][i]]
        else:
            return False

        return new_dict

    """
    This function clears all the entries in a list
    accepts 1 parameter: the list from the template to be cleared
    """
    def handle_clearing_template(self, widget_list):
        for key in widget_list:
            if isinstance(widget_list[key], Text):
                widget_list[key].delete(1.0, END)
            elif isinstance(widget_list[key], StringVar):
                widget_list[key].set(None)
            else:
                widget_list[key].delete(0, END)





