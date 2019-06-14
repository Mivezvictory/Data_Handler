import Tkinter as tk
from Tkinter import *
from pandas import DataFrame
from DataGenerators import DataAppProcessing
#TODO: rename template to match with other templates once constructed
#TODO: give each template a unique ID, for identification when opening files


class DataApp:
    # class variables for building UI labels and entry boxes
    label_width = 0.15
    label_height = 0.0325
    entry_width = 0.07
    entry_height = 0.03

    # class variables for UI layout
    entry_boldness = 1
    label_font = ("", 12)
    label_color = "white"
    entry_color = "white"

    # list of all widgets created on each page
    # helps with collecting information from each UI. And easy use of loop to get all widget entries
    widget_list = {}

    def __init__(self, parent, controller):
        self.master = parent
        self.my_controller = controller
        self.my_frame = tk.Frame(self.master, bg='#d9d9d9')  # creates a frame for this UI
        self.my_frame.place(relwidth=1, relheight=1)
        self.data_processor = DataAppProcessing.DataAppProcessing()
        self.build_template()  # builds the template

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method uses a global value for the width and height of both the labels and entry boxes
    def build_data_entry(self, label_string, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=DataApp.label_width, relheight=DataApp.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos + DataApp.label_width, rely=y_pos, relwidth=DataApp.entry_width,
                    relheight=DataApp.entry_height)
        DataApp.widget_list.update({label_string: entry})

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method is used to build labels and entry boxes that have custom width and height
    def build_data_spec(self, label_string, label_width, entry_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=DataApp.label_height)

        entry = tk.Entry(self.my_frame,  bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos + label_width, rely=y_pos, relwidth=entry_width, relheight=DataApp.entry_height)

        DataApp.widget_list.update({label_string: entry})

    # builds both a label
    # accepts the label string, width, and the x and y coordinates
    # This method is used to build labels only
    def build_label(self, label_string, label_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=DataApp.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=DataApp.label_height)

    # builds an entry box
    # accepts the label string, width, and the x and y coordinates
    # This method is used to build entry boxes only
    def build_entry(self, label_string, entry_width, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=DataApp.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=DataApp.entry_height)
        DataApp.widget_list.update({label_string: entry})

    # builds an text box for user notes
    # accepts the x and y positions of the box
    # This method is used to build text boxes only
    def build_note_text(self, x_pos, y_pos):
        note = Text(self.my_frame)
        note.place(relx=x_pos, rely=y_pos, relwidth=DataApp.entry_width * 5.25, relheight=DataApp.entry_height * 3)
        DataApp.widget_list.update({"Notes": note})

    #  a
    @classmethod
    def handle_forward_button(cls, filename):
        test = {}
        data_processor = DataAppProcessing.DataAppProcessing()
        for key in DataApp.widget_list:
            test[key] = data_processor.get_widget_entry(DataApp.widget_list[key])
        data_processor.create_csv_file(test, filename)
        return test

    def test(self):
        # print DataApp.widget_list
        for key in DataApp.widget_list:
            if isinstance(DataApp.widget_list[key], Text):
                DataApp.widget_list[key].insert(END,
                                                "This is an actual note that sadly will not be saved to the csv file, atleast not yet. (SMILLING) while listening to the travelling wilburys")
            else:
                DataApp.widget_list[key].insert(0, "Waterpen Station")

    @classmethod
    def handle_loading_template(self, csv_file):
        retrun_val = False
        data_processor = DataAppProcessing.DataAppProcessing()
        file_dict = data_processor.read_file(csv_file)
        if file_dict:
            for key in file_dict:
                # TODO: fix the problem when reading values from files. printing 0 in front of column values
                # TODO: Error comming from the way value is being read from csv file to dictionary
                if isinstance(DataApp.widget_list[key], Text):
                    DataApp.widget_list[key].insert(END, file_dict[key])
                else:
                    DataApp.widget_list[key].insert(2, file_dict[key])
            retrun_val = True

        return retrun_val

    def build_template(self):
        init_x = 0
        init_y = 0
        # 1st column
        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + DataApp.entry_height)

        self.build_data_entry("Station", init_x, init_y)

        self.build_data_entry("ChemID", 0, y_axis[2])
        self.build_data_entry("Bottle#", 0, y_axis[3])

        self.build_data_entry("Arrival time", 0, y_axis[5])
        self.build_data_entry("Departure", 0, y_axis[6])
        self.build_data_entry("Depth(m)", 0, y_axis[7])
        self.build_data_entry("Lowe depth(m)", 0, y_axis[8])
        self.build_data_entry("Lowe temp(c)", 0, y_axis[9])

        fourth_row_x = init_x + (DataApp.label_width / 1.5)
        self.build_data_entry("Analyst Name", init_x, y_axis[11])

        self.build_data_entry("Flurometer depth(m)", init_x, y_axis[12])
        self.build_data_entry("Time on", init_x, y_axis[13])
        self.build_data_entry("Time off", init_x, y_axis[14])
        self.build_data_entry("Serial No.", init_x, y_axis[15])

        self.build_data_entry("Analyst Name", init_x, y_axis[17])
        self.build_data_entry("Secchi Depth", init_x, y_axis[18])

        self.build_data_entry("Analyst Name", init_x, y_axis[20])
        self.build_data_entry("Air temperature", init_x, y_axis[21])
        self.build_data_entry("Surface temperature", init_x, y_axis[22])
        self.build_data_entry("Surface sample time", init_x, y_axis[23])
        self.build_data_entry("Bottle temperature", init_x, y_axis[24])
        self.build_data_entry("Bottle sample depth", init_x, y_axis[25])
        self.build_data_entry("Bottom bottle ID", init_x, y_axis[26])

        self.build_label("Notes: ", fourth_row_x, init_x, y_axis[28])
        self.build_note_text(init_x + DataApp.label_width, y_axis[28])

        # second column
        middle_row_x = DataApp.label_width + DataApp.entry_width + DataApp.label_width/2
        self.build_data_entry("Date", middle_row_x, init_y)

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[3])
        self.build_data_entry("Phytoplankton sample", middle_row_x, y_axis[4])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[6])
        self.build_data_entry("Zooplankton depth(m)", middle_row_x, y_axis[7])
        self.build_data_entry("Formalin added", middle_row_x, y_axis[8])
        self.build_data_entry("Vodka added", middle_row_x, y_axis[9])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[11])
        self.build_data_entry("Wave Ht(m)", middle_row_x, y_axis[12])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[14])
        self.build_label("Toxin Sample: Whole Water", DataApp.label_width, middle_row_x, y_axis[15])
        self.build_label("Toxin Sample: Zoonet", DataApp.label_width, middle_row_x, y_axis[16])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[18])
        self.build_data_entry("CBM sample", middle_row_x, y_axis[19])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[21])
        self.build_label("Weather Conditions ", DataApp.label_width, middle_row_x, y_axis[22])

        self.build_data_entry("Mainly Clear(1-4 tenths)", middle_row_x, y_axis[23])
        self.build_data_entry("Mostly Cloudy(5-9 tenths)", middle_row_x, y_axis[24])
        self.build_data_entry("Cloudy(10 tenths)", middle_row_x, y_axis[25])
        self.build_data_entry("Beaufort Wind Scale", middle_row_x, y_axis[26])

        # third column
        final_column_x = middle_row_x + DataApp.label_width + DataApp.entry_width + DataApp.label_width / 2
        self.build_data_entry("Latitude", final_column_x, init_y)

        self.build_data_entry("Longitude", final_column_x, y_axis[2])

        # rows of entry of the Y axis

        self.build_data_spec("CTD (Idronaut) profiles. Serial No.", 0.2, 0.05, final_column_x, y_axis[4])
        self.build_data_spec("Depth", 0.2, 0.05, final_column_x, y_axis[5])

        ctd_width = 0.1
        label_text = ["Cast#", " On ", " Off ", " m "]
        for i in range(0, 4):
            self.build_label(label_text[i], ctd_width, final_column_x + (ctd_width * i), y_axis[6])

        self.build_label("1.", ctd_width, final_column_x, y_axis[7])
        self.build_label("2.", ctd_width, final_column_x, y_axis[8])
        self.build_label("3.", ctd_width, final_column_x, y_axis[9])

        for i in range(1, 4):
            self.build_entry("cast1" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[7])
            self.build_entry("cast2" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[8])
            self.build_entry("cast3" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[9])

        par_width = ctd_width * 4.25
        self.build_label("PAR profiles", par_width, final_column_x, y_axis[11])
        self.build_label("Depth(m)", ctd_width, final_column_x, y_axis[12])
        self.build_label(" value 1 ", ctd_width, final_column_x + ctd_width, y_axis[12])
        self.build_label(" value 2 ", ctd_width, final_column_x + (ctd_width * 2), y_axis[12])

        par_values = ["Air", "0.10", "0.50", "1.00", "1.50", "2.00", "2.50", "3.00", "3.50", "4.00", "4.50", "5.00",
                      "5.50", "6.00", "6.50", "7.00", "7.50", "Air2"]
        for i in range(13, 13 + len(par_values)):
            pos = i - 12

            self.build_label(par_values[i - 13], ctd_width, final_column_x, y_axis[i])
            self.build_entry("PAR profiles" + str(pos) + "1", ctd_width, final_column_x + ctd_width, y_axis[i])
            self.build_entry("PAR profiles" + str(pos) + "2", ctd_width, final_column_x + (ctd_width * 2), y_axis[i])

        button_x = middle_row_x * 1.5

        back_button = tk.Button(self.my_frame, text="Back", bg="#ff0000", fg="#34495E",
                                font=10, command=lambda: self.my_controller.show_frame("StartPage"))
        back_button.place(relx=button_x, rely=y_axis[33], relwidth=DataApp.label_width / 2,
                          relheight=DataApp.label_height)

        forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E", font=10,
                                   command=self.test)
        forward_button.place(relx=button_x + 0.01 + DataApp.label_width / 2, rely=y_axis[33],
                             relwidth=DataApp.label_width / 2, relheight=DataApp.label_height)
