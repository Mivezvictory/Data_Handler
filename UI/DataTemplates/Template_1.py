import Tkinter as tk
from Tkinter import *
from DataGenerators import TemplateDataProcessor
import tkMessageBox
import csv
import json



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
        self.load_station_info()

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
                           relwidth=DataApp.label_width , relheight=DataApp.entry_height)
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

    def load_station_info(self):
        #open the csv file
        csv_file = open('C:\Users\Miyen-Ebi Iyakoregha\Desktop\work\Data_collector_info_files\station_data.csv','rU')
        #parse the csv file into json
        reader = csv.DictReader(csv_file)#, fieldnames=("Station", "New_Station_ID", "Latitude", "Longitude"))
        out = json.dumps([row for row in reader], indent=4)
        csv_file = open('C:\Users\Miyen-Ebi Iyakoregha\PycharmProjects\Data_Handler\DataGenerators\station_info.json',
                        'w')
        csv_file.write(out)

    def open_json(self):
        with open("C:\Users\Miyen-Ebi Iyakoregha\PycharmProjects\Data_Handler\DataGenerators\station_info.json", "r")\
                as data_file:
            return json.load(data_file)



    def load_lat_long(self):
        json_file = self.open_json()

        station_name = self.data_processor.get_widget_entry(DataApp.widget_list["Station Name"])
        alternate_name = self.data_processor.get_widget_entry(DataApp.widget_list["Alt. Name"])
        if station_name == "None" and alternate_name == "None":
            tkMessageBox.showinfo("Title", "Please select a valid station name and try again")
            DataApp.widget_list["Latitude"].delete(0, END)
            DataApp.widget_list["Longitude"].delete(0, END)
        elif station_name != "None" and alternate_name != "None":
            tkMessageBox.showinfo("Title", "Please select a either a station name or an alternate station name, you "
                                           "cannot select both")
            DataApp.widget_list["Latitude"].delete(0, END)
            DataApp.widget_list["Longitude"].delete(0, END)
        elif station_name == "None" and alternate_name != "None":
            for i in range(0, len(json_file)):
                item = json_file[i]
                if item["New_Station_ID"] == alternate_name:
                    if len(item["Latitude_DD"]) != 0 and len(item["Longitude_DD"]) != 0:
                        print "found"
                        DataApp.widget_list["Latitude"].delete(0, END)
                        DataApp.widget_list["Longitude"].delete(0, END)
                        DataApp.widget_list["Latitude"].insert(0, item["Latitude_DD"])
                        DataApp.widget_list["Longitude"].insert(0, item["Longitude_DD"])

                    else:
                        DataApp.widget_list["Latitude"].delete(0, END)
                        DataApp.widget_list["Longitude"].delete(0, END)
                        tkMessageBox.showinfo("Title",
                                              "This station's Latitude and Longitude are not available")

        elif station_name != "None" and alternate_name == "None":
            for i in range(0, len(json_file)):
                item = json_file[i]
                if item["Station"] == station_name:
                    print "found"
                    if len(item["Latitude_DD"]) != 0 and len(item["Longitude_DD"]) != 0:

                        DataApp.widget_list["Latitude"].delete(0, END)
                        DataApp.widget_list["Longitude"].delete(0, END)
                        DataApp.widget_list["Latitude"].insert(0, item["Latitude_DD"])
                        DataApp.widget_list["Longitude"].insert(0, item["Longitude_DD"])
                    else:
                        DataApp.widget_list["Latitude"].delete(0, END)
                        DataApp.widget_list["Longitude"].delete(0, END)
                        tkMessageBox.showinfo("Title",
                                              "This station's Latitude and Longitude are not available")

        #TODO: complete this method

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
        self.build_template()

    def build_template(self):
        init_x = 0
        init_y = 0
        # 1st column
        y_axis = {}
        for i in range(2, 35):
            y_axis[i] = (i - 1) * (init_y + DataApp.entry_height)

        station_name = ["None"]
        alt_station_name = ["None"]

        json_file = self.open_json()
        for i in range(0, len(json_file)):
            if len(json_file[i]["Station"]) != 0 and len(json_file[i]["New_Station_ID"]) != 0:
                station_name.append(json_file[i]["Station"])
                alt_station_name.append(json_file[i]["New_Station_ID"])
            elif len(json_file[i]["Station"]) != 0 and len(json_file[i]["New_Station_ID"]) == 0:
                station_name.append(json_file[i]["Station"])
            elif len(json_file[i]["Station"]) != 0 and len(json_file[i]["New_Station_ID"]) == 0:
                alt_station_name.append(json_file[i]["New_Station_ID"])

        #self.build_data_entry("Station Name", init_x, init_y)
        self.build_label("Station Name", DataApp.label_width, init_x, init_y)
        self.build_drop_down("Station Name", station_name, init_x + DataApp.label_width, init_y, DataApp.entry_width)

        self.build_label("Alt. Name", DataApp.label_width, init_x, y_axis[2])
        self.build_drop_down("Alt. Name", alt_station_name, init_x + DataApp.label_width, y_axis[2],
                             DataApp.entry_width)
        self.build_data_entry("Bottle#", 0, y_axis[3])

        self.build_data_entry("Arrival time", 0, y_axis[5])
        self.build_data_entry("Departure", 0, y_axis[6])
        self.build_data_entry("Station Depth(m)", 0, y_axis[7])
        self.build_data_entry("Lowe depth(m)", 0, y_axis[8])
        self.build_data_entry("Lowe temp(c)", 0, y_axis[9])

        fourth_row_x = init_x + (DataApp.label_width / 1.5)
        self.build_label("Analyst Name", DataApp.label_width, init_x, y_axis[11])
        self.build_drop_down("Analyst Name 1", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             init_x + DataApp.label_width, y_axis[11], DataApp.entry_width)


        self.build_data_entry("Flurometer depth(m)", init_x, y_axis[12])
        self.build_data_entry("Time on", init_x, y_axis[13])
        self.build_data_entry("Time off", init_x, y_axis[14])
        self.build_data_entry("Serial No.", init_x, y_axis[15])
        self.build_data_entry("#Casts", init_x, y_axis[16])

        self.build_label("Analyst Name", DataApp.label_width, init_x, y_axis[18])
        self.build_drop_down("Analyst Name 2", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             init_x + DataApp.label_width, y_axis[18], DataApp.entry_width)

        self.build_data_entry("Secchi Depth(m)", init_x, y_axis[19])

        self.build_label("Analyst Name", DataApp.label_width, init_x, y_axis[21])
        self.build_drop_down("Analyst Name 3", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             init_x + DataApp.label_width, y_axis[21], DataApp.entry_width)
        self.build_data_entry("Air temperature(C)", init_x, y_axis[22])
        self.build_data_entry("Surface temperature(C)", init_x, y_axis[23])
        self.build_data_entry("Surface sample time", init_x, y_axis[24])
        self.build_data_entry("Bottom temperature(C)", init_x, y_axis[25])
        self.build_data_entry("Bottom sample depth(m)", init_x, y_axis[26])
        self.build_data_entry("Bottom bottle ID", init_x, y_axis[27])

        self.build_label("Notes", fourth_row_x, init_x, y_axis[29])
        self.build_note_text(init_x + DataApp.label_width, y_axis[29])

        # second column
        middle_row_x = DataApp.label_width + DataApp.entry_width + DataApp.label_width/2
        self.build_data_entry("Date", middle_row_x, init_y)

        #self.build_data_entry("Seabird Zmax(m)", middle_row_x, y_axis[3])

        self.build_label("Analyst Name", DataApp.label_width, middle_row_x, y_axis[5])
        self.build_drop_down("Analyst Name 4", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             middle_row_x + DataApp.label_width, y_axis[5], DataApp.entry_width)
        self.build_label("Phytoplankton Sample", DataApp.label_width, middle_row_x, y_axis[6])
        self.build_drop_down("Phytoplankton Sample", ["None", "Schinct.", "Net"], middle_row_x + DataApp.label_width,
                             y_axis[6], DataApp.entry_width)

        self.build_label("Analyst Name", DataApp.label_width, middle_row_x, y_axis[8])
        self.build_drop_down("Analyst Name 5", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             middle_row_x + DataApp.label_width, y_axis[8], DataApp.entry_width)

        self.build_data_entry("Zooplankton depth(m)", middle_row_x, y_axis[9])
        self.build_label("Formalin added", DataApp.label_width, middle_row_x, y_axis[10])
        self.build_drop_down("Formalin added", ["No", "Yes"], middle_row_x + DataApp.label_width, y_axis[10],
                             DataApp.entry_width)

        self.build_label("Analyst Name", DataApp.label_width, middle_row_x, y_axis[12])
        self.build_drop_down("Analyst Name 6", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             middle_row_x + DataApp.label_width, y_axis[12], DataApp.entry_width)
        self.build_label("Toxin Sample", DataApp.label_width, middle_row_x, y_axis[13])
        self.build_drop_down("Toxin Sample", ["None", "Whole Water", "Zoonet"], middle_row_x + DataApp.label_width, y_axis[13],
                             DataApp.entry_width)

        self.build_label("Analyst Name", DataApp.label_width, middle_row_x, y_axis[15])
        self.build_drop_down("Analyst Name 7", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             middle_row_x + DataApp.label_width, y_axis[15], DataApp.entry_width)
        self.build_label("CBM sample", DataApp.label_width, middle_row_x, y_axis[16])
        self.build_drop_down("CBM sample", ["No", "Yes"], middle_row_x + DataApp.label_width, y_axis[16],
                             DataApp.entry_width)

        self.build_label("MBProv-AIS taken", DataApp.label_width, middle_row_x, y_axis[18])
        self.build_drop_down("MBProv-AIS taken", ["No", "Yes"], middle_row_x + DataApp.label_width, y_axis[18],
                             DataApp.entry_width)

        self.build_label("Analyst Name", DataApp.label_width, middle_row_x, y_axis[20])
        self.build_drop_down("Analyst Name 8", ["Claire Herbert", "Katelyn Rodgers", "Greg McCullough"],
                             middle_row_x + DataApp.label_width, y_axis[20], DataApp.entry_width)
        self.build_label("Weather Conditions ", DataApp.label_width, middle_row_x, y_axis[21])

        weather_labels = ["Clear(0 tenths)", "Mainly Clear(1-4 tenths)", "Mostly Cloudy(5-9 tenths)","Cloudy(10 tenths)"
                          ]
        self.build_radiobutton("Weather Conditions", weather_labels, middle_row_x , y_axis[22])

        wind_scale = ["0, Calm, Less than 1", "1, Light Air, 1-3", "2, Light Breeze, 4-6", "3, Gentle Breeze, 7-10",
                      "4, Moderate Breeze, 11-16", "5, Fresh Breeze, 17-21", "6, Strong Breeze, 22-27",
                      "7, Near Gale, 28-33", "8, Gale, 34-40", "9, Strong Gale, 41-47", "10, Storm, 48-55",
                      "11, Violent Storm, 56-63", "12, Hurricane, 64+"]

        self.build_data_entry("Wave Ht(m)", middle_row_x, y_axis[26])
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
        on_off_width = ctd_width/2
        self.build_label("CTD data collected", DataApp.label_width, final_column_x, y_axis[4])
        self.build_drop_down("CTD data collected", ["Yes", "No"], DataApp.label_width + final_column_x, y_axis[4],
                             DataApp.label_width/2)
        self.build_data_spec("CTD (Idronaut) profiles. Serial No.", 0.2, 0.05, final_column_x, y_axis[5])
        self.build_data_spec("Depth", 0.2, 0.05, final_column_x, y_axis[6])

        label_text_entry = ["Cast#", " On ", " Off ", " Comments "]
        for i in range(0, 4):
            self.build_label(label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[7])

        self.build_label("1.", ctd_width, final_column_x, y_axis[8])
        self.build_label("2.", ctd_width, final_column_x, y_axis[9])
        self.build_label("3.", ctd_width, final_column_x, y_axis[10])

        for i in range(1, 4):
            self.build_entry("Cast1 " + label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[8])
            self.build_entry("Cast2 " + label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[9])
            self.build_entry("Cast3 " + label_text_entry[i], ctd_width, final_column_x + (ctd_width * i), y_axis[10])

        par_width = ctd_width * 4.25
        self.build_label("PAR profiles collected", DataApp.label_width, final_column_x, y_axis[12])
        self.build_drop_down("PAR profiles collected", ["Yes", "No"], DataApp.label_width + final_column_x, y_axis[12],
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

        forward_button = tk.Button(self.my_frame, text="Forward", bg="green", fg="#34495E", font=10,
                                   command=self.test)
        forward_button.place(relx=button_x + 0.01 + DataApp.label_width / 2, rely=y_axis[33],
                             relwidth=DataApp.label_width / 2, relheight=DataApp.label_height)
