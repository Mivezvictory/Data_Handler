import Tkinter as tk
from Tkinter import *


class CustomPage:
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
        self.build_template()

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method uses a global value for the width and height of both the labels and entry boxes
    def build_data_entry(self, label, x_pos, y_pos):

        label = tk.Label(self.my_frame, text=label, bg="#d9d9d9", fg="black", font=CustomPage.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=CustomPage.label_width, relheight=CustomPage.label_height)

        entry = tk.Entry(self.my_frame, bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos + CustomPage.label_width, rely=y_pos, relwidth=CustomPage.entry_width,
                    relheight=CustomPage.entry_height)

    # builds both a label and data entry box
    # accepts the label of the entry box, the x and y coordinates
    # This method is used to build labels and entry boxes that have custom width and height
    def build_data_spec(self, label, label_width, entry_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label, bg="#d9d9d9", fg="black", font=CustomPage.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=CustomPage.label_height)

        entry = tk.Entry(self.my_frame,  bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos + label_width, rely=y_pos, relwidth=entry_width, relheight=CustomPage.entry_height)

    # builds both a label
    # accepts the label text, width, and the x and y coordinates
    # This method is used to build labels only
    def build_label(self, label, label_width, x_pos, y_pos):
        label = tk.Label(self.my_frame, text=label, bg="#d9d9d9", fg="black", font=CustomPage.label_font)
        label.place(relx=x_pos, rely=y_pos, relwidth=label_width, relheight=CustomPage.label_height)

    # builds both a entry box
    # accepts the width, and the x and y coordinates
    # This method is used to build entry boxes only
    def build_entry(self, entry_width, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=CustomPage.entry_height)

    def build_note_entry(self, entry_width, entry_height, x_pos, y_pos):
        entry = tk.Entry(self.my_frame, bg="white", bd=CustomPage.entry_boldness)
        entry.place(relx=x_pos, rely=y_pos, relwidth=entry_width, relheight=entry_height)

    def build_note_text(self, x_pos, y_pos):
        note = Text(self.my_frame)
        note.place(relx=x_pos, rely=y_pos, relwidth=CustomPage.entry_width * 5.25, relheight=CustomPage.entry_height * 3)

    def build_template(self):
        init_x = 0
        init_y = 0

        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + CustomPage.entry_height)

        # 1st column
        self.build_data_entry("Station: ", init_x, init_y)
        self.build_data_entry("ChemID: ", 0, y_axis[2])
        self.build_data_entry("Bottle #: ", 0, y_axis[3])

        data_entry_text = ["Arrival time: ", "Departure: ", "Depth (m): ", "Lowe depth(m): ", "Lowe temp(c): "]
        for i in range(5, 10):
            self.build_data_entry(data_entry_text[i - 5], 0, y_axis[i])

        fourth_row_x = init_x + (CustomPage.label_width / 1.5)
        self.build_data_entry("Analyst Name: ", init_x, y_axis[11])
        label_1 = ["flurometer depth(m): ", "Time on: ", "Time off: ", "serial no. "]
        for i in range(12, 16):
            self.build_data_entry(label_1[i - 12], init_x, y_axis[i])

        self.build_data_entry("Analyst Name: ", init_x, y_axis[17])
        self.build_data_entry(" Secchi Depth: ", init_x, y_axis[18])

        self.build_data_entry("Analyst Name: ", init_x, y_axis[20])
        self.build_data_entry(" Air Temperature: ", init_x, y_axis[21])
        self.build_data_entry(" Surface Temperature: ", init_x, y_axis[22])
        self.build_data_entry(" Surface Sample Time: ", init_x, y_axis[23])
        self.build_data_entry(" Bottle Temperature: ", init_x, y_axis[24])
        self.build_data_entry(" Bottle Sample Depth: ", init_x, y_axis[25])
        self.build_data_entry(" Bottom Bottle ID: ", init_x, y_axis[26])

        self.build_label("Notes: ", fourth_row_x, init_x, y_axis[28])
        self.build_note_text(init_x + CustomPage.label_width, y_axis[28])

        # second column
        middle_row_x = CustomPage.label_width + CustomPage.entry_width + CustomPage.label_width/2
        self.build_data_entry("Date: ", middle_row_x, init_y)

        self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[3])
        self.build_data_entry("Phytoplankton Sample: ", middle_row_x, y_axis[4])

        self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[6])
        self.build_data_entry(" Zooplankton Depth(m): ", middle_row_x, y_axis[7])
        self.build_data_entry(" Formalin added: ", middle_row_x, y_axis[8])
        self.build_data_entry(" Vodka added: ", middle_row_x, y_axis[9])

        self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[11])
        self.build_data_entry(" Wave Ht(m): ", middle_row_x, y_axis[12])

        self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[14])
        self.build_label("Toxin Sample: Whole Water", CustomPage.label_width, middle_row_x, y_axis[15])
        self.build_label("Toxin Sample: Zoonet", CustomPage.label_width, middle_row_x, y_axis[16])

        self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[18])
        self.build_data_entry(" CBM Sample ", middle_row_x, y_axis[19])

        self.build_data_entry("Analyst Name: ", middle_row_x, y_axis[21])
        self.build_label(" Weather Conditions ", CustomPage.label_width, middle_row_x, y_axis[22])

        self.build_data_entry(" Mainly Clear (1-4 tenths)", middle_row_x, y_axis[23])
        self.build_data_entry("Mostly Cloudy(5-9 tenths)", middle_row_x, y_axis[24])
        self.build_data_entry(" Cloudy (10 tenths)", middle_row_x, y_axis[25])
        self.build_data_entry(" Beaufort Wind Scale", middle_row_x, y_axis[26])

        # third column
        final_column_x = middle_row_x + CustomPage.label_width + CustomPage.entry_width + CustomPage.label_width / 2
        self.build_data_entry("Latitude: ", final_column_x, init_y)

        self.build_data_entry("Longitude: ", final_column_x, y_axis[2])

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
        self.back_button.place(relx=button_x, rely=y_axis[33], relwidth=CustomPage.label_width/2, relheight=CustomPage.label_height)

        self.forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E",font=10)
        # command=lambda: self.my_controller.show_frame("StartPage"))
        self.forward_button.place(relx=button_x + 0.01 + CustomPage.label_width/2, rely=y_axis[33], relwidth=CustomPage.label_width / 2,
                               relheight=CustomPage.label_height)