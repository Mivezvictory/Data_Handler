import Tkinter as tk
from Tkinter import *
from pandas import DataFrame
from DataGenerators import TemplateDataProcessor
from UI.WidgetTemplates import Menu_Sample


# TODO: rename template to match with other templates once constructed
# TODO: give each template a unique ID, for identification when opening files


class Template_3:
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
    template_identifier = "Template_3"

    # list of all widgets created on each page
    # helps with collecting information from each UI. And easy use of loop to get all widget entries
    widget_list = {}

    def __init__(self, parent, controller):
        self.master = parent
        self.my_controller = controller
        self.my_frame = tk.Frame(self.master, bg='#d9d9d9')  # creates a frame for this UI
        self.my_frame.place(relwidth=1, relheight=1)
        self.data_processor = TemplateDataProcessor.TemplateDataProcessor()

        self.build_template()  # builds the template

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method uses a global value for the width and height of both the labels and entry boxes
    def build_data_entry(self, label_string, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=Template_3.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=Template_3.label_width, relheight=Template_3.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=Template_3.entry_boldness)
        entry.place(relx=x_pos + Template_3.label_width, rely=y_pos, relwidth=Template_3.entry_width,
                    relheight=Template_3.entry_height)
        Template_3.widget_list.update({label_string: entry})

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method is used to build labels and entry boxes that have custom width and height
    def build_data_spec(self, label_string, label_width, entry_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=Template_3.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=Template_3.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=Template_3.entry_boldness)
        entry.place(relx=x_pos + label_width, rely=y_pos, relwidth=entry_width, relheight=Template_3.entry_height)

        Template_3.widget_list.update({label_string: entry})

    # builds both a label
    # accepts the label string, width, and the x and y coordinates
    # This method is used to build labels only
    def build_label(self, label_string, label_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label_string, bg="#d9d9d9", fg="black", font=Template_3.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=Template_3.label_height)

    # builds an entry box
    # accepts the label string, width, and the x and y coordinates
    # This method is used to build entry boxes only
    def build_entry(self, label_string, entry_width, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=Template_3.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=Template_3.entry_height)
        Template_3.widget_list.update({label_string: entry})

    # builds an text box for user notes
    # accepts the x and y positions of the box
    # This method is used to build text boxes only
    def build_note_text(self, x_pos, y_pos):
        note = Text(self.my_frame)
        note.place(relx=x_pos, rely=y_pos, relwidth=Template_3.entry_width * 3.25,
                   relheight=Template_3.entry_height * 8)
        Template_3.widget_list.update({"Notes": note})

    def build_drop_down(self, label, options, x_pos, y_pos, width):
        variable = StringVar(self.master)
        variable.set(options[0])  # default value

        w = apply(OptionMenu, (self.my_frame, variable) + tuple(options))
        w.pack()

        w.place(relx=x_pos, rely=y_pos, relwidth=width,
                               relheight=Template_3.entry_height)
        Template_3.widget_list.update({label: w})

    def test(self):
        self.handle_clearing_template()
        # TODO: should clear the current contents of the entry boxes before populating it
        # print Template_3.widget_list
        for key in Template_3.widget_list:
            if isinstance(Template_3.widget_list[key], Text):
                Template_3.widget_list[key].insert(END,
                                                   "This is an actual note that sadly will not be saved to the csv file, "
                                                   "atleast not yet. (SMILLING)while listening to the travelling wilburys")
            else:
                Template_3.widget_list[key].insert(0, "Waterpen Station")

    @classmethod
    def populate_template(self, key, string):
        # print Template_3.widget_list
        if isinstance(Template_3.widget_list[key], Text):
            Template_3.widget_list[key].insert(END, string)
        else:
            Template_3.widget_list[key].insert(0, string)

    def printV(self):
        print("this is a test")

    """
    #  a
    @classmethod
    def handle_forward_button(cls, filename):
        test = {}
        data_processor = Template_3Processing.Template_3Processing()
        for key in Template_3.widget_list:
            test[key] = data_processor.get_widget_entry(Template_3.widget_list[key])
        data_processor.create_csv_file(test, filename)
        return test

    @classmethod
    def handle_loading_template(cls, csv_file):
        cls.handle_clearing_template()
        retrun_val = False
        data_processor = Template_3Processing.Template_3Processing()
        file_dict = data_processor.read_file(csv_file)
        if file_dict:
            for key in file_dict:
                if isinstance(Template_3.widget_list[key], Text):
                    Template_3.widget_list[key].insert(END, file_dict[key])
                else:
                    Template_3.widget_list[key].insert(0, file_dict[key])
            retrun_val = True
        return retrun_val
        """

    def handle_clearing_template(self):
        self.data_processor.handle_clearing_template(Template_3.widget_list)

    def build_template(self):
        init_x = 0
        init_y = 0
        # 1st column
        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + Template_3.entry_height)

        self.build_data_entry("Station", init_x, init_y)
        self.build_data_entry("Bottle ID", 0, y_axis[2])

        self.build_data_entry("Arrival time", 0, y_axis[5])
        self.build_data_entry("Departure", 0, y_axis[6])

        self.build_data_entry("Analyst Name", init_x, y_axis[8])
        self.build_data_entry("CTD Depth(m)", 0, y_axis[9])
        self.build_data_entry("Time On", 0, y_axis[10])
        self.build_data_entry("Time Off", init_x, y_axis[12])
        self.build_data_entry("Serial No.", 0, y_axis[13])

        fourth_row_x = init_x + (Template_3.label_width / 1.5)
        self.build_data_entry("Analyst Name", init_x, y_axis[15])
        self.build_label("Phytoplankton Sample: Schinct. Net", Template_3.label_width * 1.5, init_x , y_axis[16])

        self.build_data_entry("Analyst Name", init_x, y_axis[18])
        self.build_label("CBM Sample", Template_3.label_width, init_x, y_axis[19])
        self.build_drop_down("CBM Sample", ["Yes", "No"], init_x + Template_3.label_width, y_axis[19], Template_3.entry_width)

        self.build_data_entry("Analyst Name", init_x, y_axis[21])
        self.build_label("Weather Conditions ", Template_3.label_width, init_x, y_axis[22])
        self.build_data_entry("Mainly Clear(1-4 tenths)", init_x, y_axis[23])
        self.build_data_entry("Mostly Cloudy(5-9 tenths)", init_x, y_axis[24])
        self.build_data_entry("Cloudy(10 tenths)", init_x, y_axis[25])
        self.build_data_entry("Beaufort Wind Scale", init_x, y_axis[26])

        # second column
        middle_row_x = Template_3.label_width + Template_3.entry_width + Template_3.label_width / 4
        ctd_width = 0.1
        self.build_data_entry("Date", middle_row_x, init_y)

        self.build_label("Position", Template_3.entry_width, middle_row_x, y_axis[5])
        postion_text = ["Center", "North", "East", "South", "West"]

        for i in range(1, 4):
            self.build_drop_down("pos_1", postion_text, middle_row_x + (Template_3.entry_width * i), y_axis[5],
                                 Template_3.entry_width)

        self.build_label("DTW", Template_3.entry_width, middle_row_x, y_axis[6])
        for i in range(1, 4):
            self.build_entry("DTW" + str(i), Template_3.entry_width, middle_row_x + (Template_3.entry_width * i),
                             y_axis[6])

        self.build_label("DOW", Template_3.entry_width, middle_row_x, y_axis[8])
        for i in range(1, 4):
            self.build_entry("DOW1" + str(i), Template_3.entry_width, middle_row_x + (Template_3.entry_width * i),
                             y_axis[8])
            self.build_entry("DOW2" + str(i), Template_3.entry_width, middle_row_x + (Template_3.entry_width * i),
                             y_axis[9])
            self.build_entry("DOW3" + str(i), Template_3.entry_width, middle_row_x + (Template_3.entry_width * i),
                             y_axis[10])

        self.build_label("Directions", Template_3.entry_width, middle_row_x, y_axis[13])
        postion_text = ["N to S", "S to N", "E to W", "W to E"]

        for i in range(1, 4):
            self.build_drop_down("Directions", postion_text, middle_row_x + (Template_3.entry_width * i), y_axis[13],
                                 Template_3.entry_width)

        self.build_label("WOW", Template_3.entry_width, middle_row_x, y_axis[16])
        for i in range(1, 4):
            self.build_entry("WOW" + str(i), Template_3.entry_width, middle_row_x + (Template_3.entry_width * i),
                             y_axis[16])

        self.build_label("Notes: ", fourth_row_x, middle_row_x - 0.01, y_axis[19])
        self.build_note_text(middle_row_x + Template_3.entry_width, y_axis[19])

        # third column
        final_column_x = middle_row_x + Template_3.label_width + Template_3.entry_width + Template_3.label_width / 1.5
        self.build_data_entry("Latitude", final_column_x, init_y)

        self.build_data_entry("Longitude", final_column_x, y_axis[2])

        # rows of entry of the Y axis

        self.build_label("Flow/Velocity", Template_3.label_width, final_column_x, y_axis[5])
        self.build_data_spec("Length of flow measurement", 0.2, 0.05, final_column_x, y_axis[6])

        self.build_label("Position", ctd_width, final_column_x, y_axis[7])
        postion_text = ["Center", "North", "East", "South", "West"]

        for i in range(1, 4):
            self.build_drop_down("pos_1", postion_text, final_column_x + (ctd_width * i), y_axis[7], ctd_width)

        self.build_label("time 1", ctd_width, final_column_x, y_axis[8])
        self.build_label("time 2", ctd_width, final_column_x, y_axis[9])
        self.build_label("time 3", ctd_width, final_column_x, y_axis[10])

        for i in range(1, 4):
            self.build_entry("time1" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[8])
            self.build_entry("time2" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[9])
            self.build_entry("time3" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[10])

        self.build_label("Flow/Velocity", Template_3.label_width, final_column_x, y_axis[13])
        self.build_data_spec("Length of flow measurement", 0.2, 0.05, final_column_x, y_axis[14])

        ctd_width = 0.1
        self.build_label("Position", ctd_width, final_column_x, y_axis[15])
        postion_text = ["Center", "North", "East", "South", "West"]

        for i in range(1, 4):
            self.build_drop_down("pos_1", postion_text, final_column_x + (ctd_width * i), y_axis[15], ctd_width)

        self.build_label("time 1", ctd_width, final_column_x, y_axis[16])
        self.build_label("time 2", ctd_width, final_column_x, y_axis[17])
        self.build_label("time 3", ctd_width, final_column_x, y_axis[18])

        for i in range(1, 4):
            self.build_entry("time1" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[16])
            self.build_entry("time2" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[17])
            self.build_entry("time3" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[18])

        self.build_label("Flow/Velocity", Template_3.label_width, final_column_x, y_axis[21])
        self.build_data_spec("Length of flow measurement", 0.2, 0.05, final_column_x, y_axis[22])

        ctd_width = 0.1
        self.build_label("Position", ctd_width, final_column_x, y_axis[23])
        postion_text = ["Center", "North", "East", "South", "West"]

        for i in range(1, 4):
            self.build_drop_down("pos_1", postion_text, final_column_x + (ctd_width * i), y_axis[23], ctd_width)

        self.build_label("time 1", ctd_width, final_column_x, y_axis[24])
        self.build_label("time 2", ctd_width, final_column_x, y_axis[25])
        self.build_label("time 3", ctd_width, final_column_x, y_axis[26])

        for i in range(1, 4):
            self.build_entry("time1" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[24])
            self.build_entry("time2" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[25])
            self.build_entry("time3" + str(i), ctd_width, final_column_x + (ctd_width * i), y_axis[26])

        button_x = middle_row_x * 1.5

        back_button = tk.Button(self.my_frame, text="Back", bg="#ff0000", fg="#34495E",
                                font=10, command=lambda: self.my_controller.show_frame("StartPage"))
        back_button.place(relx=button_x, rely=y_axis[33], relwidth=Template_3.label_width / 2,
                          relheight=Template_3.label_height)

        forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E", font=10,
                                   command=self.test)
        forward_button.place(relx=button_x + 0.01 + Template_3.label_width / 2, rely=y_axis[33],
                             relwidth=Template_3.label_width / 2, relheight=Template_3.label_height)
