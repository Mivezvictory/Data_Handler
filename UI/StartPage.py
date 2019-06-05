import tkinter as tk


class StartPage:
    def __init__(self, parent, controller):

        # The parent will be the main frame of the DataEntry Object (DataEntry.my_containter_frame),
        # which this will be placed into.
        # The controller argument is the DataEntry object itself
        self.parent = parent
        self.my_controller = controller

        # A frame is an invisible box that we put stuff into.
        # Pack the frame up and place a label
        self.my_frame = tk.Frame(self.parent, bg="pink")
        self.my_frame.pack(fill=tk.BOTH, expand=True)
        self.label = tk.Label(self.my_frame, text="Welcome to the avocado clan lads", font=12)
        self.label.pack(pady=10, padx=10)

        init_x = 0.3
        init_y = 0.3
        button_width = 0.4
        button_height = 0.05

        # Make the button in the middle, and assign the command argument to load a different page.
        # my_controller.show_frame loads up the new frame.
        # TODO: See below
        """ TODO: Make this more modular instead of using 'DataApp' and 'MetaDataHandler_Sample' as literals,
            have them as constants in their respective classes and just import them and use class.Variable containing 
            the name to get it."""
        self.load_template_button = tk.Button(self.my_frame, text="Load a template", bg="#EAECEE", fg="#34495E",
                                              font=10, command=lambda: self.my_controller.show_frame("DataApp"))
        self.load_template_button.place(relx=init_x, rely=init_y, relwidth=button_width, relheight=button_height)
        self.load_template_button.config(highlightbackground="black")

        self.load_other_template_button = tk.Button(self.my_frame, text="Load the other Template", bg="#EAECEE", fg="#34495E",
                                              font=10, command=lambda: self.my_controller.show_frame("MetaHandler_Sample"))
        self.load_other_template_button.place(relx=init_x, rely=init_y+0.3, relwidth=button_width, relheight=button_height)
        self.load_other_template_button.config(highlightbackground="black")


        #load_template.pack()