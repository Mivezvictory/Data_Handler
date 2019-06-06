import tkinter as tk


class StartPage:
    button_width = 0.5
    button_height = 0.05
    def __init__(self, parent, controller):

        # The parent will be the main frame of the DataEntry Object (DataEntry.my_containter_frame),
        # which this will be placed into.
        # The controller argument is the DataEntry object itself
        self.parent = parent
        self.my_controller = controller

        # A frame is an invisible box that we put stuff into.
        # Pack the frame up and place a label
        self.my_frame = tk.Frame(self.parent, bg="white")
        self.my_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.my_frame, text="Welcome to CEOS data & metadata collector", font=12)
        self.label.pack(pady=10, padx=10)

        # Make the button in the middle, and assign the command argument to load a different page.
        # my_controller.show_frame loads up the new frame.
        # TODO: See below
        """ TODO: Make this more modular instead of using 'DataApp' and 'MetaDataHandler_Sample' as literals,
            have them as constants in their respective classes and just import them and use class.Variable containing 
            the name to get it."""
        init_x = 0.25
        init_y = 0.3
        self.build_button("Load a template", "DataApp", init_x, init_y)
        self.build_button("Load Metadata Handler", "MetaHandler_Sample", init_x, init_y + 0.01 + StartPage.button_height)
        about_botton_y =  init_y + 0.02 + (StartPage.button_height * 2)
        self.build_button("About","dummy", init_x, about_botton_y)

    def build_button(self, text, command, x_pos, y_pos):
        self.load_template_button = tk.Button(self.my_frame, text=text, bg="#EAECEE", fg="#34495E",
                                              font=10, command=lambda: self.my_controller.show_frame(command))
        self.load_template_button.place(relx=x_pos, rely=y_pos, relwidth=StartPage.button_width,
                                        relheight=StartPage.button_height)
        self.load_template_button.config(highlightbackground="black")



        #load_template.pack()