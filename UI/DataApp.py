import Tkinter as tk
from Tkinter import *
from DataGenerators import DataAppProcessing
#TODO: rename template to match with other templates once constructed
#TODO: give each template a unique ID, for identification when opening files

class DataApp():
    label_width = 0.15
    label_height = 0.0325

    entry_width = 0.07
    entry_height = 0.03
    entry_boldness = 1
    label_font = ("", 12)
    label_color = "white"
    entry_color = "white"

    def __init__(self, parent, controller):

        #self.menuBar = BuildMenu.BuildMenu(parent)
        #self.menuBar.build_menu()
        #self.build_menu()
        height = 650
        width = 1200
        #self.minsize(width, height)
        self.master = parent
        self.my_controller = controller
        self.my_frame = tk.Frame(self.master, bg='#d9d9d9')
        self.my_frame.place(relwidth=1, relheight=1)
        #self.data_processor = DataAppProcessing.DataAppProcessing()
        self.build_template()

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method uses a global value for the width and height of both the labels and entry boxes
    def build_data_entry(self, label, x_pos, y_pos):

        label = tk.Label(self.my_frame, text=label, bg="#d9d9d9", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=DataApp.label_width, relheight=DataApp.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos + DataApp.label_width, rely=y_pos, relwidth=DataApp.entry_width,
                    relheight=DataApp.entry_height)
        return entry

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method is used to build labels and entry boxes that have custom width and height
    def build_data_spec(self, label, label_width, entry_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label, bg="#d9d9d9", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=DataApp.label_height)

        entry = tk.Entry(self.my_frame,  bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos + label_width, rely=y_pos, relwidth=entry_width, relheight=DataApp.entry_height)

        return entry

    # builds both a label
    # accepts the label text, width, and the x and y coordinates
    # This method is used to build labels only
    def build_label(self, label, label_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label, bg="#d9d9d9", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=DataApp.label_height)

    # builds both a entry box
    # accepts the width, and the x and y coordinates
    # This method is used to build entry boxes only
    def build_entry(self, entry_width, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=DataApp.entry_height)

        return entry

    def build_note_entry(self, entry_width, entry_height, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=entry_height)

        return entry

    def build_note_text(self, x_pos, y_pos):
        note = Text(self.my_frame)
        note.place(relx=x_pos, rely=y_pos, relwidth=DataApp.entry_width * 5.25, relheight=DataApp.entry_height * 3)

        return note

    def handle_forward_button(self):
        station = self.data_processor.get_widget_entry(self.station)
        chemID = self.data_processor.get_widget_entry(self.chemID)
        bootle_num = self.data_processor.get_widget_entry(self.bottle_num)
        arrival_time = self.data_processor.get_widget_entry(self.arrival_time)

        departure = self.data_processor.get_widget_entry(self.departure)
        depth = self.data_processor.get_widget_entry(self.depth)
        lowe_depth = self.data_processor.get_widget_entry(self.lowe_depth)
        lowe_temp = self.data_processor.get_widget_entry(self.lowe_temp)

        analyst_name1 = self.data_processor.get_widget_entry(self.analyst_name1)
        flurometer_depth = self.data_processor.get_widget_entry(self.flurometer_depth)
        time_on = self.data_processor.get_widget_entry(self.time_on)
        time_off = self.data_processor.get_widget_entry(self.time_off)
        serial_no = self.data_processor.get_widget_entry(self.serial_no)

        analyst_name2 = self.data_processor.get_widget_entry(self.analyst_name2)
        secci_depth = self.data_processor.get_widget_entry(self.secci_depth)

        analyst_name3 = self.data_processor.get_widget_entry(self.analyst_name3)
        air_temp = self.data_processor.get_widget_entry(self.air_temprature)
        surface_temp = self.data_processor.get_widget_entry(self.surface_temprature)
        surface_sample_time = self.data_processor.get_widget_entry(self.surface_sample_time)
        bottle_temp = self.data_processor.get_widget_entry(self.bottle_temperature)
        bottle_sample_depth = self.data_processor.get_widget_entry(self.bottle_sample_depth)
        bottom_bottleID =  self.data_processor.get_widget_entry(self.bottom_bottleID)

        notes =  self.data_processor.get_widget_entry(self.notes)

        date = self.data_processor.get_widget_entry(self.date)

        analyst_name4 = self.data_processor.get_widget_entry(self.analyst_name4)
        phytoplankton = self.data_processor.get_widget_entry(self.phytoplankton_sample)

        analyst_name5 = self.data_processor.get_widget_entry(self.analyst_name5)
        zooplankton = self.data_processor.get_widget_entry(self.zooplankton_depth)
        formalin = self.data_processor.get_widget_entry(self.formalin)
        vodka = self.data_processor.get_widget_entry(self.vodka)

        analyst_name6 = self.data_processor.get_widget_entry(self.analyst_name6)
        wave = self.data_processor.get_widget_entry(self.wave)

        analyst_name7 = self.data_processor.get_widget_entry(self.analyst_name7)

        analyst_name8 = self.data_processor.get_widget_entry(self.analyst_name8)
        CBN = self.data_processor.get_widget_entry(self.CBM)

        analyst_name9 = self.data_processor.get_widget_entry(self.analyst_name9)
        clear = self.data_processor.get_widget_entry(self.clear)
        mostly_cloudy = self.data_processor.get_widget_entry(self.mostly_cloudy)
        cloudy = self.data_processor.get_widget_entry(self.cloudy)
        wind_scale = self.data_processor.get_widget_entry(self.wind_scale)

        latitude = self.data_processor.get_widget_entry(self.latitude)
        longitude = self.data_processor.get_widget_entry(self.longitude)

    def build_template(self):
        init_x = 0
        init_y = 0
        # 1st column
        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + DataApp.entry_height)

        self.station = self.build_data_entry("Station: ", init_x, init_y)

        self.chemID = self.build_data_entry("ChemID: ", 0, y_axis[2])
        self.bottle_num = self.build_data_entry("Bottle #: ", 0, y_axis[3])

        self.arrival_time = self.build_data_entry("Arrival time: ", 0, y_axis[5])
        self.departure = self.build_data_entry("Departure: ", 0, y_axis[6])
        self.depth = self.build_data_entry("Depth (m): ", 0, y_axis[7])
        self.lowe_depth = self.build_data_entry("Lowe depth(m): ", 0, y_axis[8])
        self.lowe_temp = self.build_data_entry("Lowe temp(c): ", 0, y_axis[9])

        fourth_row_x = init_x + (DataApp.label_width / 1.5)
        self.analyst_name1 = self.build_data_entry("Analyst Name: ", init_x, y_axis[11])

        self.flurometer_depth = self.build_data_entry("flurometer depth(m): ", init_x, y_axis[12])
        self.time_on = self.build_data_entry("Time on: ", init_x, y_axis[13])
        self.time_off = self.build_data_entry("Time off: ", init_x, y_axis[14])
        self.serial_no = self.build_data_entry("serial no. ", init_x, y_axis[15])

        self.analyst_name2 = self.build_data_entry("Analyst Name: ", init_x, y_axis[17])
        self.secci_depth = self.build_data_entry(" Secchi Depth: ", init_x, y_axis[18])

        self.analyst_name3 = self.build_data_entry("Analyst Name: ", init_x, y_axis[20])
        self.air_temprature = self.build_data_entry(" Air Temperature: ", init_x, y_axis[21])
        self.surface_temprature = self.build_data_entry(" Surface Temperature: ", init_x, y_axis[22])
        self.surface_sample_time = self.build_data_entry(" Surface Sample Time: ", init_x, y_axis[23])
        self.bottle_temperature = self.build_data_entry(" Bottle Temperature: ", init_x, y_axis[24])
        self.bottle_sample_depth = self.build_data_entry(" Bottle Sample Depth: ", init_x, y_axis[25])
        self.bottom_bottleID = self.build_data_entry(" Bottom Bottle ID: ", init_x, y_axis[26])

        self.build_label("Notes: ", fourth_row_x, init_x, y_axis[28])
        self.notes = self.build_note_text(init_x + DataApp.label_width, y_axis[28])

        # second column
        middle_row_x = DataApp.label_width + DataApp.entry_width + DataApp.label_width/2
        self.date = self.build_data_entry("Date: ", middle_row_x, init_y)

        self.analyst_name4 = self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[3])
        self.phytoplankton_sample = self.build_data_entry("Phytoplankton Sample: ", middle_row_x, y_axis[4])

        self.analyst_name5 = self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[6])
        self.zooplankton_depth = self.build_data_entry(" Zooplankton Depth(m): ", middle_row_x, y_axis[7])
        self.formalin = self.build_data_entry(" Formalin added: ", middle_row_x, y_axis[8])
        self.vodka = self.build_data_entry(" Vodka added: ", middle_row_x, y_axis[9])

        self.analyst_name6 = self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[11])
        self.wave = self.build_data_entry(" Wave Ht(m): ", middle_row_x, y_axis[12])

        self.analyst_name7 = self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[14])
        self.build_label("Toxin Sample: Whole Water", DataApp.label_width, middle_row_x, y_axis[15])
        self.build_label("Toxin Sample: Zoonet", DataApp.label_width, middle_row_x, y_axis[16])

        self.analyst_name8 = self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[18])
        self.CBM = self.build_data_entry(" CBM Sample ", middle_row_x, y_axis[19])

        self.analyst_name9 = self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[21])
        self.build_label(" Weather Conditions ", DataApp.label_width, middle_row_x, y_axis[22])

        self.clear = self.build_data_entry(" Mainly Clear (1-4 tenths)", middle_row_x, y_axis[23])
        self.mostly_cloudy = self.build_data_entry("Mostly Cloudy(5-9 tenths)", middle_row_x, y_axis[24])
        self.cloudy = self.build_data_entry(" Cloudy (10 tenths)", middle_row_x, y_axis[25])
        self.wind_scale = self.build_data_entry(" Beaufort Wind Scale", middle_row_x, y_axis[26])

        # third column
        final_column_x = middle_row_x + DataApp.label_width + DataApp.entry_width + DataApp.label_width / 2
        self.latitude = self.build_data_entry("Latitude: ", final_column_x, init_y)

        self.longitude = self.build_data_entry("Longitude: ", final_column_x, y_axis[2])

        # rows of entry of the Y axis

        self.build_data_spec("CTD (Idronaut) profiles. Serial No. ", 0.2, 0.05, final_column_x, y_axis[4])
        self.build_data_spec("Depth : ", 0.2, 0.05, final_column_x, y_axis[5])

        ctd_width = 0.1
        label_text = ["Cast#", " On ", " Off ", " m "]
        for i in range(0, 4):
            self.build_label(label_text[i], ctd_width, final_column_x + (ctd_width * i), y_axis[6])

        self.build_label("1.", ctd_width, final_column_x, y_axis[7])
        self.build_label("2.", ctd_width, final_column_x, y_axis[8])
        self.build_label("3.", ctd_width, final_column_x, y_axis[9])

        for i in range(1, 4):
            self.build_entry(ctd_width, final_column_x + (ctd_width * i), y_axis[7])
            self.build_entry(ctd_width, final_column_x + (ctd_width * i), y_axis[8])
            self.build_entry(ctd_width, final_column_x + (ctd_width * i), y_axis[9])

        par_width = ctd_width * 4.25
        self.build_label("PAR profiles", par_width, final_column_x, y_axis[11])
        self.build_label("Depth(m)", ctd_width, final_column_x, y_axis[12])
        self.build_label(" value 1 ", ctd_width, final_column_x + ctd_width, y_axis[12])
        self.build_label(" value 2 ", ctd_width, final_column_x + (ctd_width * 2), y_axis[12])

        par_values = ["Air", "0.10", "0.50", "1.00", "1.50", "2.00", "2.50", "3.00", "3.50", "4.00", "4.50", "5.00",
                      "5.50", "6.00", "6.50", "7.00", "7.50", "Air2"]
        for i in range(13, 13 + len(par_values)):
            self.build_label(par_values[i - 13], ctd_width, final_column_x, y_axis[i])
            self.build_entry(ctd_width, final_column_x + ctd_width, y_axis[i])
            self.build_entry(ctd_width, final_column_x + (ctd_width * 2), y_axis[i])

        button_x = middle_row_x * 1.5
        self.back_button = tk.Button(self.my_frame, text="Back", bg="#ff0000", fg="#34495E",
                                     font=10, command=lambda: self.my_controller.show_frame("StartPage"))
        self.back_button.place(relx=button_x, rely=y_axis[33], relwidth=DataApp.label_width / 2,
                               relheight=DataApp.label_height)

        self.forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E", font=10)
        # command=lambda: self.my_controller.show_frame("StartPage"))
        self.forward_button.place(relx=button_x + 0.01 + DataApp.label_width / 2, rely=y_axis[33],
                                  relwidth=DataApp.label_width / 2,
                                  relheight=DataApp.label_height)