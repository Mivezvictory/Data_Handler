import Tkinter as tk
from Tkinter import *
from DataGenerators import TemplateDataProcessor


#TODO: rename template to match with other templates once constructed
#TODO: give each template a unique ID, for identification when opening files


class DataApp:
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
    template_identifier = "DataApp"
    template_number = 0

    # list of all widgets created on each page
    # helps with collecting information from each UI. And easy use of loop to get all widget entries
    widget_list = {}

    def __init__(self,  parent, controller, my_frames):
        self.master = parent
        self.my_controller = controller
        self.my_frame = tk.Frame(self.master, bg='#ffffff')  # creates a frame for this UI
        self.my_frame.place(relwidth=1, relheight=1)
        self.build_template()  # builds the template
        self.data_processor = TemplateDataProcessor.TemplateDataProcessor()

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
        note = Text(self.my_frame, bd=DataApp.entry_boldness)
        note.place(relx=x_pos, rely=y_pos, relwidth=DataApp.entry_width * 5.25, relheight=DataApp.entry_height * 3)
        DataApp.widget_list.update({"Notes": note})

    def build_drop_down(self, label, options, x_pos, y_pos, width):
        variable = StringVar(self.master)
        variable.set(options[0])  # default value

        w = apply(OptionMenu, (self.my_frame, variable) + tuple(options))
        w.pack()

        w.place(relx=x_pos, rely=y_pos, relwidth=width,
                relheight=DataApp.entry_height)
        DataApp.widget_list.update({label: variable})

    def build_radiobutton(self, label, options, x_pos, y_pos):
        variable = StringVar(self.master)
        variable.set("None")  # default value
        count = 0
        for text in options:
            r_button = Radiobutton(self.my_frame, text=text, variable=variable, value=text, indicatoron=False)
            r_button.place(relx=x_pos, rely=y_pos+count,
                           relwidth=DataApp.entry_width * 1.5, relheight=DataApp.entry_height)
            count += DataApp.entry_height

        DataApp.widget_list.update({label: variable})

    def test(self):
        self.handle_clearing_template()
        # print DataApp.widget_list
        for key in DataApp.widget_list:
            if isinstance(DataApp.widget_list[key], Text):
                DataApp.widget_list[key].insert(END,
                                                "This is an actual note that sadly will not be saved to the csv file, "
                                                "atleast not yet. (SMILLING)while listening to the travelling wilburys")
            elif isinstance(DataApp.widget_list[key], StringVar):
                print (" no need to fix this")
            else:
                DataApp.widget_list[key].insert(0, "Waterpen Station")

    # populates the templates data entries with data from a dictionary
    # accepts 2 parameters, a key, and a dictionary for which the key is valid
    def populate_template(self, dictionary, key):
        # print DataApp.widget_list
        if isinstance(DataApp.widget_list[key], Text):
            DataApp.widget_list[key].insert(END, dictionary[key])
        elif isinstance(DataApp.widget_list[key], StringVar):
            DataApp.widget_list[key].set(dictionary[key])
        else:
            DataApp.widget_list[key].insert(0, dictionary[key])

    def save_data_entries(self, filename):
        test = {}
        for key in DataApp.widget_list:
            test[key] = self.data_processor.get_widget_entry(DataApp.widget_list[key])
        self.data_processor.create_csv_file(test, filename[0], DataApp.template_number)
        if test["PAR profiles collected"] == "Yes":
            self.data_processor.create_csv_file(test, filename[5], 6)
        if test["CTD data collected"] == "Yes":
            self.data_processor.create_csv_file(test, filename[4], 7)
        return test

    def open_saved_files(self, csv_file):
        self.handle_clearing_template()
        retrun_val = False

        file_dict = self.data_processor.read_file(csv_file, DataApp.template_number)
        if file_dict:
            for key in file_dict:
                self.populate_template(file_dict, key)
            retrun_val = True
        return retrun_val

    # clears the template
    def handle_clearing_template(self):
        self.data_processor.handle_clearing_template(DataApp.widget_list)

    def build_template(self):
        init_x = 0
        init_y = 0
        # 1st column
        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + DataApp.entry_height)

        self.build_data_entry("Station", init_x, init_y)
        self.build_data_entry("Bottle#", 0, y_axis[2])

        self.build_data_entry("Arrival time", 0, y_axis[5])
        self.build_data_entry("Departure", 0, y_axis[6])
        self.build_data_entry("Depth(m)", 0, y_axis[7])
        self.build_data_entry("Lowe depth(m)", 0, y_axis[8])
        self.build_data_entry("Lowe temp(c)", 0, y_axis[9])

        fourth_row_x = init_x + (DataApp.label_width / 1.5)
        self.build_data_entry("Analyst Name 1", init_x, y_axis[11])

        self.build_data_entry("Flurometer depth(m)", init_x, y_axis[12])
        self.build_data_entry("Time on", init_x, y_axis[13])
        self.build_data_entry("Time off", init_x, y_axis[14])
        self.build_data_entry("Serial No.", init_x, y_axis[15])
        self.build_data_entry("#Casts", init_x, y_axis[16])

        self.build_data_entry("Analyst Name 2", init_x, y_axis[18])
        self.build_data_entry("Secchi Depth", init_x, y_axis[19])

        self.build_data_entry("Analyst Name 3", init_x, y_axis[21])
        self.build_data_entry("Air temperature", init_x, y_axis[22])
        self.build_data_entry("Surface temperature", init_x, y_axis[23])
        self.build_data_entry("Surface sample time", init_x, y_axis[24])
        self.build_data_entry("Bottle temperature", init_x, y_axis[25])
        self.build_data_entry("Bottle sample depth", init_x, y_axis[26])
        self.build_data_entry("Bottom bottle ID", init_x, y_axis[27])

        self.build_label("Notes", fourth_row_x, init_x, y_axis[29])
        self.build_note_text(init_x + DataApp.label_width, y_axis[29])

        # second column
        middle_row_x = DataApp.label_width + DataApp.entry_width + DataApp.label_width/2
        self.build_data_entry("Date", middle_row_x, init_y)

        self.build_data_entry("Analyst Name 4", middle_row_x, y_axis[3])
        self.build_label("Phytoplankton Sample", DataApp.label_width, middle_row_x, y_axis[4])
        self.build_drop_down("Phytoplankton Sample", ["Schinct.", "Net"], middle_row_x + DataApp.label_width, y_axis[4],
                             DataApp.entry_width)

        self.build_data_entry("Analyst Name 5", middle_row_x, y_axis[6])
        self.build_data_entry("Zooplankton depth(m)", middle_row_x, y_axis[7])
        self.build_data_entry("Formalin added", middle_row_x, y_axis[8])

        self.build_data_entry("Analyst Name 6", middle_row_x, y_axis[11])
        self.build_data_entry("Wave Ht(m)", middle_row_x, y_axis[12])

        self.build_data_entry("Analyst Name 7", middle_row_x, y_axis[14])
        self.build_label("Toxin Sample", DataApp.label_width, middle_row_x, y_axis[15])
        self.build_drop_down("Toxin Sample", ["Whole Water", "Zoonet"], middle_row_x + DataApp.label_width, y_axis[15],
                             DataApp.entry_width)

        self.build_data_entry("Analyst Name 8", middle_row_x, y_axis[18])
        self.build_data_entry("CBM sample", middle_row_x, y_axis[19])

        self.build_data_entry("Analyst Name 9", middle_row_x, y_axis[21])
        self.build_label("Weather Conditions ", DataApp.label_width, middle_row_x, y_axis[22])

        weather_labels = ["Clear(0 tenths)","Mainly Clear(1-4 tenths)", "Mostly Cloudy(5-9 tenths)", "Cloudy(10 tenths)"
                          ]
        self.build_radiobutton("Weather Conditions", weather_labels, middle_row_x + DataApp.label_width, y_axis[22])

        wind_scale = ["Calm", "Light Air", "Light Breeze", "Gentle Breeze", "Moderate Breeze",
                      "Fresh Breeze", "Strong Breeze", "Near Gale", "Gale", "Strong Gale", "Storm"]

        self.build_label("Beaufort Wind Scale", DataApp.label_width, middle_row_x, y_axis[27])
        self.build_drop_down("Beaufort Wind Scale", wind_scale, middle_row_x + DataApp.label_width, y_axis[27],
                             DataApp.entry_width)

        #self.build_data_entry("Mainly Clear(1-4 tenths)", middle_row_x, y_axis[23])
        #self.build_data_entry("Mostly Cloudy(5-9 tenths)", middle_row_x, y_axis[24])
        #self.build_data_entry("Cloudy(10 tenths)", middle_row_x, y_axis[25])
        #self.build_data_entry("Beaufort Wind Scale", middle_row_x, y_axis[26])

        # third column
        final_column_x = middle_row_x + DataApp.label_width + DataApp.entry_width + DataApp.label_width / 2
        self.build_data_entry("Latitude", final_column_x, init_y)

        self.build_data_entry("Longitude", final_column_x, y_axis[2])

        # rows of entry of the Y axis
        ctd_width = 0.1
        self.build_label("CTD data collected", DataApp.label_width, final_column_x, y_axis[4])
        self.build_drop_down("CTD data collected", ["No", "Yes"], DataApp.label_width + final_column_x, y_axis[4],
                             DataApp.label_width/2)
        self.build_data_spec("CTD (Idronaut) profiles. Serial No.", 0.2, 0.05, final_column_x, y_axis[5])
        self.build_data_spec("Depth", 0.2, 0.05, final_column_x, y_axis[6])

        label_text = ["Cast#", " On ", " Off ", " m "]
        label_text_entry = ["Cast#", "On", "Off", "Depth"]
        for i in range(0, 4):
            self.build_label(label_text[i], ctd_width, final_column_x + (ctd_width * i), y_axis[7])

        self.build_label("1.", ctd_width, final_column_x, y_axis[8])
        self.build_label("2.", ctd_width, final_column_x, y_axis[9])
        self.build_label("3.", ctd_width, final_column_x, y_axis[10])

        for i in range(1, 4):
            self.build_entry("Cast1 " + label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[8])
            self.build_entry("Cast2 " + label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[9])
            self.build_entry("Cast3 " + label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[10])

        par_width = ctd_width * 4.25
        self.build_label("PAR profiles collected", DataApp.label_width, final_column_x, y_axis[12])
        self.build_drop_down("PAR profiles collected", ["No", "Yes"], DataApp.label_width + final_column_x, y_axis[12],
                             DataApp.label_width / 2)
        #self.build_label("PAR profiles", par_width, final_column_x, y_axis[12])
        self.build_label("Depth(m)", ctd_width, final_column_x, y_axis[13])
        self.build_label(" value 1 ", ctd_width, final_column_x + ctd_width, y_axis[13])
        self.build_label(" value 2 ", ctd_width, final_column_x + (ctd_width * 2), y_axis[13])

        par_values = ["Air", "0.10", "0.50", "1.00", "1.50", "2.00", "2.50", "3.00", "3.50", "4.00", "4.50", "5.00",
                      "5.50", "6.00", "6.50", "7.00", "7.50", "Air2"]
        for i in range(14, 14 + len(par_values)):
            pos = i - 13

            self.build_label(par_values[i - 14], ctd_width, final_column_x, y_axis[i])
            self.build_entry(par_values[i - 14] + " " + "Value 1", ctd_width, final_column_x + ctd_width, y_axis[i])
            self.build_entry(par_values[i - 14] + " " + "Value 2", ctd_width, final_column_x + (ctd_width * 2), y_axis[i])

        button_x = middle_row_x * 1.5

        back_button = tk.Button(self.my_frame, text="Back", bg="#cccccc", fg="#34495E",
                                font=10, command=lambda: self.my_controller.show_frame("StartPage"))
        back_button.place(relx=button_x, rely=y_axis[33], relwidth=DataApp.label_width / 2,
                          relheight=DataApp.label_height)

        #forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E", font=10,
                                   #command=self.test)
        #forward_button.place(relx=button_x + 0.01 + DataApp.label_width / 2, rely=y_axis[33],
                             #relwidth=DataApp.label_width / 2, relheight=DataApp.label_height)
