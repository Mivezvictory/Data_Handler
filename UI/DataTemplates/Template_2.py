import Tkinter as tk
from Tkinter import *
from DataGenerators import DataAppProcessing

class CustomPage:
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
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=CustomPage.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=CustomPage.label_width, relheight=CustomPage.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos + CustomPage.label_width, rely=y_pos, relwidth=CustomPage.entry_width,
                    relheight=CustomPage.entry_height)
        CustomPage.widget_list.update({label_string: entry})

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method is used to build labels and entry boxes that have custom width and height
    def build_data_spec(self, label_string, label_width, entry_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=CustomPage.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=CustomPage.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos + label_width, rely=y_pos, relwidth=entry_width, relheight=CustomPage.entry_height)

        CustomPage.widget_list.update({label_string: entry})

    # builds both a label
    # accepts the label string, width, and the x and y coordinates
    # This method is used to build labels only
    def build_label(self, label_string, label_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=CustomPage.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=CustomPage.label_height)

    # builds an entry box
    # accepts the label string, width, and the x and y coordinates
    # This method is used to build entry boxes only
    def build_entry(self, label_string, entry_width, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=CustomPage.entry_height)
        CustomPage.widget_list.update({label_string: entry})

    # builds an text box for user notes
    # accepts the x and y positions of the box
    # This method is used to build text boxes only
    def build_note_text(self, x_pos, y_pos):
        note = Text(self.my_frame)
        note.place(relx=x_pos, rely=y_pos, relwidth=CustomPage.entry_width * 5.25, relheight=CustomPage.entry_height * 3)
        CustomPage.widget_list.update({"Notes": note})

    def test(self):
        self.handle_clearing_template()
        # TODO: should clear the current contents of the entry boxes before populating it
        # print CustomPage.widget_list
        for key in CustomPage.widget_list:
            if isinstance(CustomPage.widget_list[key], Text):
                CustomPage.widget_list[key].insert(END,
                                                "This is an actual note that sadly will not be saved to the csv file, "
                                                "atleast not yet. (SMILLING)while listening to the travelling wilburys")
            else:
                CustomPage.widget_list[key].insert(0, "Waterpen Station")

    @classmethod
    def populate_template(self, key, string):
        # print CustomPage.widget_list
        if isinstance(CustomPage.widget_list[key], Text):
            CustomPage.widget_list[key].insert(END, string)
        else:
            CustomPage.widget_list[key].insert(0, string)

    #  a
    @classmethod
    def handle_forward_button(cls, filename):
        test = {}
        data_processor = DataAppProcessing.DataAppProcessing()
        for key in CustomPage.widget_list:
            test[key] = data_processor.get_widget_entry(CustomPage.widget_list[key])
        data_processor.create_csv_file(test, filename)
        return test

    @classmethod
    def handle_loading_template(cls, csv_file):
        cls.handle_clearing_template()
        retrun_val = False
        data_processor = DataAppProcessing.DataAppProcessing()
        file_dict = data_processor.read_file(csv_file)
        if file_dict:
            for key in file_dict:
                if isinstance(CustomPage.widget_list[key], Text):
                    CustomPage.widget_list[key].insert(END, file_dict[key])
                else:
                    CustomPage.widget_list[key].insert(0, file_dict[key])
            retrun_val = True
        return retrun_val

    @classmethod
    def handle_clearing_template(cls):
        for key in CustomPage.widget_list:
            if isinstance(CustomPage.widget_list[key], Text):
                CustomPage.widget_list[key].delete(1.0, END)
            else:
                CustomPage.widget_list[key].delete(0, END)

    def build_template(self):
        init_x = 0
        init_y = 0

        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + CustomPage.entry_height)

        self.build_data_entry("Station", init_x, init_y)
        self.build_data_entry("ChemID", 0, y_axis[2])
        self.build_data_entry("Bottle#", 0, y_axis[3])

        self.build_data_entry("Arrival Time", 0, y_axis[5])
        self.build_data_entry("Departure", 0, y_axis[6])
        self.build_data_entry("Depth(m)", 0, y_axis[7])

        fourth_row_x = init_x + (CustomPage.label_width / 1.5)
        self.build_data_entry("Analyst Name", init_x, y_axis[9])
        self.build_data_entry("Brancker Logger Depth(m)", init_x, y_axis[10])
        self.build_data_entry("Time On", init_x, y_axis[11])
        self.build_data_entry("Time Off", init_x, y_axis[12])

        self.build_data_entry("Analyst Name", init_x, y_axis[14])
        self.build_data_entry("Secchi Depth", init_x, y_axis[15])

        self.build_data_entry("Analyst Name", init_x, y_axis[17])
        self.build_data_entry("Air Temperature", init_x, y_axis[18])
        self.build_data_entry("Surface Temperature", init_x, y_axis[19])
        self.build_data_entry("Surface Sample Time", init_x, y_axis[20])
        self.build_data_entry("250 ml Nutrients(#)", init_x, y_axis[21])
        self.build_data_entry("Phytoplankton Sample", init_x, y_axis[22])

        self.build_data_entry("Analyst Name", init_x, y_axis[24])
        self.build_data_entry("Phytoplankton Depth", init_x, y_axis[25])
        self.build_data_entry("Analyst Name", init_x, y_axis[26])
        self.build_data_entry("Discreet Zoohaul Depth(m)", init_x, y_axis[27])

        self.build_label("Notes: ", fourth_row_x, init_x, y_axis[29])
        self.build_note_text(init_x + CustomPage.label_width, y_axis[29])

        # second column
        middle_row_x = CustomPage.label_width + CustomPage.entry_width + CustomPage.label_width / 2
        self.build_data_entry("Date", middle_row_x, init_y)

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[5])
        self.build_data_entry("Benthos Samples(#)", middle_row_x, y_axis[6])
        self.build_data_entry("Meiobenthos Samples(#)", middle_row_x, y_axis[7])
        self.build_data_entry("Sediment(#)", middle_row_x, y_axis[8])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[10])
        self.build_data_entry("Plankton Net Haul(Y/N)", middle_row_x, y_axis[11])

        self.build_data_entry("Fish Trawl(Y/N)", middle_row_x, y_axis[13])
        self.build_data_entry("Depth", middle_row_x, y_axis[14])
        self.build_data_entry("Start Time", middle_row_x, y_axis[15])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[17])
        self.build_label("Weather Conditions ", CustomPage.label_width, middle_row_x, y_axis[18])

        self.build_data_entry("Mainly Clear(1-4 tenths)", middle_row_x, y_axis[19])
        self.build_data_entry("Mostly Cloudy(5-9 tenths)", middle_row_x, y_axis[20])
        self.build_data_entry("Cloudy(10 tenths)", middle_row_x, y_axis[21])
        self.build_data_entry("Beaufort Wind Scale", middle_row_x, y_axis[22])

        self.build_data_entry("Yawl Station(Y/N)", middle_row_x, y_axis[24])

        self.build_data_entry("Analyst Name", middle_row_x, y_axis[26])
        self.build_data_entry("Extra Sample", middle_row_x, y_axis[27])


        # third column
        final_column_x = middle_row_x + CustomPage.label_width + CustomPage.entry_width + CustomPage.label_width / 2
        self.build_data_entry("Latitude", final_column_x, init_y)

        self.build_data_entry("Longitude", final_column_x, y_axis[2])

        # rows of entry of the Y axis

        profile_width = 0.1
        self.build_label("Profiles", profile_width, final_column_x + profile_width, y_axis[5])
        label_text = ["Depth", "O2", "Light"]
        for i in range(0, 3):
            self.build_label(label_text[i], profile_width, final_column_x + (profile_width * i), y_axis[6])

        for i in range(7, 28):
            self.build_entry("cast1" + str(i), profile_width, final_column_x + (profile_width * 0), y_axis[i])
            self.build_entry("cast2" + str(i), profile_width, final_column_x + (profile_width * 1), y_axis[i])
            self.build_entry("cast3" + str(i), profile_width, final_column_x + (profile_width * 2), y_axis[i])

        button_x = middle_row_x * 1.5

        back_button = tk.Button(self.my_frame, text="Back", bg="#ff0000", fg="#34495E",
                                font=10, command=lambda: self.my_controller.show_frame("StartPage"))
        back_button.place(relx=button_x, rely=y_axis[33], relwidth=CustomPage.label_width / 2,
                          relheight=CustomPage.label_height)

        forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E", font=10,
                                   command=self.test)
        forward_button.place(relx=button_x + 0.01 + CustomPage.label_width / 2, rely=y_axis[33],
                             relwidth=CustomPage.label_width / 2, relheight=CustomPage.label_height)