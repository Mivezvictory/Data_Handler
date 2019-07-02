import Tkinter as tk
import tkMessageBox
from UI.WidgetTemplates import Menu_Sample

class StartPage:
    button_width = 0.5
    button_height = 0.05
    template_identifier = 1
    def __init__(self, parent, controller, my_frames):

        # The parent will be the main frame of the DataEntry Object (DataEntry.my_containter_frame),
        # which this will be placed into.
        # The controller argument is the DataEntry object itself

        self.parent = parent
        self.my_controller = controller


        # A frame is an invisible box that we put stuff into.
        # Pack the frame up and place a label
        self.my_frame = tk.Frame(self.parent, bg="white")
        self.my_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.my_frame, text="Welcome to CEOS's data & metadata collector", font=12)
        self.label.pack(pady=10, padx=10)

        # Make the button in the middle, and assign the command argument to load a different page.
        # my_controller.show_frame loads up the new frame.
        # TODO: See below
        """ TODO: Make this more modular instead of using 'DataApp' and 'MetaDataHandler_Sample' as literals,
            have them as constants in their respective classes and just import them and use class.Variable containing 
            the name to get it."""

        self.template_names = {"Template 1: Team A field template for lake moon moon tapioca": "DataApp",
                               "Template 2: readings from the great pyramid of giza, writtings of Pharaoh Ramseys II":
                               "CustomPage", "Template 3: The joker finally meets the thief": "Template_3"}
        init_x = 0.25
        init_y = 0.3

        set1_y = init_y - 0.005 - StartPage.button_height
        self.drop_down_menu = tk.StringVar()
        self.drop_down_menu.set('select a template')  # set the default option

        self.set_options = tk.OptionMenu(self.my_frame, self.drop_down_menu, "Template 1: Team A field template for lake moon moon tapioca",
                                  "Template 2: readings from the great pyramid of giza, writtings of Pharaoh Ramseys II",
                                         "Template 3: The joker finally meets the thief")
        self.set_options.configure(font=("", 12), fg="#34495E")
        self.set_options.place(relx=init_x, rely=set1_y, relwidth=StartPage.button_width,
                                relheight=StartPage.button_height)

        self.build_customised_buttons("Load a template", init_x + init_x/2, init_y, StartPage.button_width/2,
                          StartPage.button_height, self.load_template)

        metaHandler_y = init_y + 0.01 + (StartPage.button_height * 2)
        self.build_button("Load Metadata Handler", "MetaHandler_Sample", init_x, metaHandler_y)
        about_botton_y =  metaHandler_y + 0.01 + StartPage.button_height
        self.build_button("Build a template", "CustomPage", init_x, about_botton_y)

    def load_template(self):
        value = self.drop_down_menu.get()
        if value == 'select a template':
            tkMessageBox.showinfo("Title", "Please select a template")

        else:
            template_name = self.template_names[value]
            self.my_controller.show_frame(template_name)

    def build_button(self, text, command, x_pos, y_pos):
        self.load_template_button = tk.Button(self.my_frame, text=text, bg="#C0C0C0", fg="#34495E",
                                              font=10, command=lambda: self.my_controller.show_frame(command))
        self.load_template_button.place(relx=x_pos, rely=y_pos, relwidth=StartPage.button_width,
                                        relheight=StartPage.button_height)
        #self.load_template_button.config(highlightbackground="black")

    def build_customised_buttons(self, text, x_pos, y_pos, width, height, command):
        self.load_template_button = tk.Button(self.my_frame, text=text, bg="#EAECEE", fg="#34495E",
                                              font=10, command=command)
        self.load_template_button.place(relx=x_pos, rely=y_pos, relwidth=width,
                                        relheight=height)
        #self.load_template_button.config(highlightbackground="black")
