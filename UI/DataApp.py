import tkinter as tk
from tkinter import *
import BuildMenu

class DataApp():
    label_width = 0.09
    label_height = 0.0325

    entry_width = 0.07
    entry_height = 0.0325
    entry_boldness = 1.25
    label_font = ("", 10)
    label_color = "white"
    entry_color = "white"

    def __init__(self, master):
        #self.controller = controller
        #self.menuBar = BuildMenu.BuildMenu(parent)
        #self.menuBar.build_menu()
        #self.build_menu()
        height = 650
        width = 1200
        #self.minsize(width, height)
        self.master = master
        frame = tk.Frame(self.master, bg='white')
        frame.place(relwidth=1, relheight=1)
        self.build_template()

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method uses a global value for the width and height of both the labels and entry boxes
    def build_data_entry(self, label, x_pos, y_pos):

        label = Label(self.master, text=label, bg="white", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=DataApp.label_width, relheight=DataApp.label_height)

        entry = Entry(self.master, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos + DataApp.label_width, rely=y_pos, relwidth=DataApp.entry_width,
                    relheight=DataApp.entry_height)

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method is used to build labels and entry boxes that have custom width and height
    def build_data_spec(self, label, label_width, entry_width, x_pos, y_pos):
        label = Label(self.master, text=label, bg="white", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=DataApp.label_height)

        entry = Entry(self.master,  bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos + label_width, rely=y_pos, relwidth=entry_width, relheight=DataApp.entry_height)

    # builds both a label
    # accepts the label text, width, and the x and y coordinates
    # This method is used to build labels only
    def build_label(self, label, label_width, x_pos, y_pos):
        label = Label(self.master, text=label, bg="white", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=DataApp.label_height)

    # builds both a entry box
    # accepts the width, and the x and y coordinates
    # This method is used to build entry boxes only
    def build_entry(self, entry_width, x_pos, y_pos):
        entry = Entry(self.master, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=DataApp.entry_height)

    def build_note_entry(self, entry_width, entry_height, x_pos, y_pos):
        entry = Entry(self.master, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=entry_height)

    def build_template(self):
        init_x = 0
        init_y = 0

        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + DataApp.entry_height)

        # 1st column
        self.build_data_entry("Station: ", init_x, init_y)
        self.build_data_entry("ChemID: ", 0, y_axis[2])
        self.build_data_entry("Bottle #: ", 0, y_axis[3])

        data_entry_text = ["Arrival time: ", "Departure: ", "Depth (m): ", "Lowe depth(m): ", "Lowe temp(c): "]
        for i in range(5, 10):
            self.build_data_entry(data_entry_text[i - 5], 0, y_axis[i])

        fourth_row_x = init_x + (DataApp.label_width / 1.5)
        self.build_entry(fourth_row_x, init_x, y_axis[11])
        label_1 = ["flurometer depth(m): ", "Time on: ", "Time off: ", "serial no. "]
        for i in range(11, 15):
            self.build_data_entry(label_1[i - 11], fourth_row_x, y_axis[i])

        self.build_entry(fourth_row_x, init_x, y_axis[16])
        self.build_data_entry(" Secchi Depth: ", fourth_row_x, y_axis[16])

        self.build_entry(fourth_row_x, init_x, y_axis[18])
        self.build_data_entry(" Air Temperature: ", fourth_row_x, y_axis[18])
        self.build_data_entry(" Surface Temperature: ", fourth_row_x, y_axis[19])
        self.build_data_entry(" Surface Sample Time: ", fourth_row_x, y_axis[20])
        self.build_data_entry(" Bottle Temperature: ", fourth_row_x, y_axis[21])
        self.build_data_entry(" Bottle Sample Depth: ", fourth_row_x, y_axis[22])
        self.build_data_entry(" Bottom Bottle ID: ", fourth_row_x, y_axis[23])

        self.build_label("Notes: ", fourth_row_x, init_x, y_axis[25])
        #self.build_note_entry(DataApp.entry_width + 0.08, 0.14, ctd_width, y_axis[25])

        # second column
        date_x = 0.015 + DataApp.label_width + DataApp.entry_width
        ctd_x = date_x * 3.7
        ctd_x = ctd_x - 0.05
        middle_row = date_x + DataApp.label_width + 0.030
        self.build_data_entry("Date: ", middle_row, init_y)

        self.build_entry(DataApp.label_width, middle_row, y_axis[4])
        self.build_data_entry(" Phytoplankton Sample: ", middle_row + DataApp.label_width, y_axis[4])

        self.build_entry(DataApp.label_width, middle_row, y_axis[5])
        self.build_data_entry(" Zooplankton Depth(m): ", middle_row + DataApp.label_width, y_axis[5])
        self.build_data_entry(" Formalin added: ", middle_row + DataApp.label_width, y_axis[6])
        self.build_data_entry(" Vodka added: ", middle_row + DataApp.label_width, y_axis[7])

        self.build_entry(DataApp.label_width, middle_row, y_axis[11])
        self.build_data_entry(" Wave Ht(m): ", middle_row + DataApp.label_width, y_axis[11])

        toxin_x = (middle_row + DataApp.label_width) - 0.020
        self.build_label("Toxin Sample: Whole Water", DataApp.label_width + DataApp.label_width, toxin_x, y_axis[12])
        self.build_entry(DataApp.label_width, middle_row, y_axis[12])

        self.build_label("Toxin Sample: Zoonet", DataApp.label_width + DataApp.label_width, toxin_x, y_axis[13])

        self.build_entry(DataApp.label_width, middle_row, y_axis[14])
        self.build_data_entry(" CBM Sample ", middle_row + DataApp.label_width, y_axis[14])

        self.build_label(" Weather Conditions: ", DataApp.label_width + DataApp.label_width, toxin_x, y_axis[18])
        self.build_entry(DataApp.label_width, middle_row, y_axis[18])
        self.build_data_entry(" Mainly Clear (1-4 tenths)", middle_row + DataApp.label_width, y_axis[20])
        self.build_data_entry("Mostly Cloudy(5-9 tenths)", middle_row + DataApp.label_width, y_axis[21])
        self.build_data_entry(" Cloudy (10 tenths)", middle_row + DataApp.label_width, y_axis[22])
        self.build_data_entry(" Beaufort Wind Scale", middle_row + DataApp.label_width, y_axis[23])
        self.build_entry(DataApp.label_width, middle_row, y_axis[23])

        self.build_data_entry("Latitude: ", ctd_x, init_y)

        self.build_data_entry("Longitude: ", ctd_x, y_axis[2])

        # rows of entry of the Y axis

        self.build_data_spec("CTD (Idronaut) profiles. Serial No. ", 0.2, 0.05, ctd_x, y_axis[4])
        self.build_data_spec("Depth : ", 0.2, 0.05, ctd_x, y_axis[5])

        ctd_width = 0.1
        label_text = ["Cast#", " On ", " Off ", " m "]
        for i in range(0, 4):
            self.build_label(label_text[i], ctd_width, ctd_x + (ctd_width * i), y_axis[6])

        self.build_label("1.", ctd_width, ctd_x, y_axis[7])
        self.build_label("2.", ctd_width, ctd_x, y_axis[8])
        self.build_label("3.", ctd_width, ctd_x, y_axis[9])

        for i in range(1, 4):
            self.build_entry(ctd_width, ctd_x + (ctd_width * i), y_axis[7])
            self.build_entry(ctd_width, ctd_x + (ctd_width * i), y_axis[8])
            self.build_entry(ctd_width, ctd_x + (ctd_width * i), y_axis[9])

        par_width = ctd_width * 4.25
        self.build_label("PAR profiles", par_width, ctd_x, y_axis[11])
        self.build_label("Depth(m)", ctd_width, ctd_x, y_axis[12])
        self.build_label(" value 1 ", ctd_width, ctd_x + ctd_width, y_axis[12])
        self.build_label(" value 2 ", ctd_width, ctd_x + (ctd_width * 2), y_axis[12])

        par_values = ["Air", "0.10", "0.50", "1.00", "1.50", "2.00", "2.50", "3.00", "3.50", "4.00", "4.50", "5.00",
                      "5.50", "6.00", "6.50", "7.00", "7.50", "Air2"]
        for i in range(13, 13 + len(par_values)):
            self.build_label(par_values[i - 13], ctd_width, ctd_x, y_axis[i])
            self.build_entry(ctd_width, ctd_x + ctd_width, y_axis[i])
            self.build_entry(ctd_width, ctd_x + (ctd_width * 2), y_axis[i])


root = Tk()
root.geometry('1200x650')
DataApp(root)
root.mainloop()
