import Tkinter as tk
from Tkinter import *
import DataEntry


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the avocado clan lads", font=12)
        label.pack(pady=10, padx=10)
        init_x = 0.3
        init_y = 0.3
        button_width = 0.4
        button_height = 0.05
        load_template = tk.Button(self, text="Load a template", bg="#EAECEE", fg="#34495E", font=10,
                               command=lambda: controller.show_frame("DataApp"))
        load_template.place(relx=init_x, rely=init_y, relwidth=button_width, relheight=button_height)
        load_template.config(highlightbackground="black")
        #load_template.pack()