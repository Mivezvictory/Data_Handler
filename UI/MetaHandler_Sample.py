import tkinter
import tkinter.ttk as tttk
from UI.WidgetTemplates import Menu_Sample, Vertical_ScrollableFrame_Sample

"""We generally need to build grids so it we'll have a function for that"""


class MetaHandler_Sample:
    def __init__(self, parent, controller):
        # Know your parent GUI handler. (In this case it will be the frame of The DataEntry Object.)
        # The controller is the DataEntry Object itself. This is needed so that the menu bar can be placed in the
        # DataEntry window which is the parent
        self.parent = parent
        self.controller = controller

        # A frame is an invisible box that we put stuff into. In this case it belongs to self.master
        # This frame will be used to hold the scrollable frame.
        # Make the frame extend to the left and right edge and expand as needed.
        self.my_frame = tkinter.Frame(self.parent, bg="pink")
        # No need to pack, since it is going to be managed by another parent frame
        #self.my_frame.pack(fill=tkinter.BOTH, expand=True, padx=1, pady=1)

        # Make the scrollable frame, and place it in the highest level frame created previously.
        # Pack it to fill both left and right edges.
        self.scrollable = Vertical_ScrollableFrame_Sample.V_ScrollableFrame_Sample(self.my_frame)
        self.scrollable.pack(fill=tkinter.BOTH, expand=True)

        # Make the mainframe which will contain the actual widgets and place it in the scrollable frames interior frame.
        # Set background color to blue and height and width at 100
        # Pack the mainframe in, the fill argument will make it take up the entire window.
        # Remember its invisible at this point, so it will not necessarily show anything besides a blue background.
        self.mainframe = tkinter.Frame(self.scrollable.interior_frame, bg="blue", height=100, width=100)
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        # Build the grid
        # Build the banner at the top of the Screen (which says CEOS METADATA now)
        # Build the buttons in the UI.
        self.build_grid()
        self.build_banner()
        self.build_buttons()

        # Build the toolbar menu at the top of the screen that has ("File, Edit...etc")
        # It needs to be hoked on the parent, because this is not in a regular frame.
        self.toolMenu = Menu_Sample.Menu_Sample(self.controller.parent)
        #self.toolMenu.build_toolmenu()


        self.make_dropdown(['Ice mass buoy', 'Ice beacon data', 'Physical Ice Sampling'])
        fields = ["Station ID", "Year", "Personnel", "Notes"]
        choices = {'Ice mass buoy', 'Ice beacon data', 'Physical Ice Sampling'}
        #choices = ['Ice mass buoy', 'Ice beacon data', 'Physical Ice Sampling']
        self.entries = self.makeform(fields)
        self.choices = self.make_dropdown(choices)
        #self.choices = self.make_combobox(choices)

        #self.master.bind('<Return>', (lambda event, e=ents: self.fetch(e)))
        #b1 = tkinter.Button(self.master, text='Show',
                    #command=(lambda e=ents: self.fetch(e)))

        #TODO: Remove this later on this is just for testing the scrolling functionality
        for row in range(4,100):
            #tkinter.Label(self.mainframe, text="%s" % row, width=3, borderwidth="1",
                     #relief="solid").grid(row=row, column=0)
            t = "this is the second column for row"
            tkinter.Button(self.mainframe, text=t).grid(row=row, column=0)

        tkinter.Button(self.mainframe, text="Back", bg="red", command=lambda: self.controller.show_frame("StartPage")).grid(row=101, column=0)

    def build_grid(self):
        """ We generally need to use a grid to put stuff together, so this function will let us build that grid."""
        # we'll have one column (column 0 the first argument) which has a weight of 1,
        #  meaning that it will resize proportionally to everything else.
        self.mainframe.columnconfigure(0, weight=1)
        # Row 0 will not resize so it will maintain its size (weight =0)
        self.mainframe.rowconfigure(0, weight=0)
        # Row 1 will resize to fit
        self.mainframe.rowconfigure(1, weight=1)
        # Row 2 will not resize
        self.mainframe.rowconfigure(2, weight=1)
        # Row 3 will not resize
        self.mainframe.rowconfigure(3, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            bg="white",
            text="CEOS METADATA",
            fg="black",
            font=('Helvetica', 24)
        )
        banner.grid(
            # specify the row and column that this banner should be located in
            row=0, column=0,
            # The stickyness will be an iterable (can be string or list) to specify where we want the thing to stick to.
            # Here we don't need to worry about it sticking to the top or bottom, so we only specify for the sides
            #  (east and west, hence the arguments 'ew') since it never gets taller
            # It could also me 'we'
            sticky='ew',
            # padx and pady specify the padding, Padding is space on the on x or y axis within that row and column,
            # where the object is located.
            padx=10, pady=5
        )

    def build_buttons(self):
        # Make frame for buttons, to be within the mainframe
        buttons_frame = tkinter.Frame(self.mainframe)
        # Place the grid for the buttons in a specific row and column of the mainframe. In this case row 3, column 0
        # Handle the stickiness, by making it stick on all sides, pad on both x and y
        buttons_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        # We only have one row, so we don't need to specify for that, so we just deal with columns
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        # Make buttons for Submit and reset
        self.submit_button = tkinter.Button(
            buttons_frame,
            text="SUBMIT"
        )
        self.reset_button = tkinter.Button(
            buttons_frame,
            text="RESET"
        )
        # Add those buttons to specific locations within the buttons frame.
        # In this case since there is only one row, place each button in one of the columns.
        # The sticky 'ew' (east west) will allow the buttons to expand as the Window grows.
        self.submit_button.grid(row=0, column=0, sticky='ew')
        self.reset_button.grid(row=0, column=1, sticky='ew')

        return

    def fetch(self, entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))

    # on change dropdown value
    def change_dropdown(self, args):
        print(self.tkvar.get())
        # link function to change dropdown
        return

    def make_dropdown(self, options):
        dropdown_frame = tkinter.Frame(self.mainframe)
        dropdown_frame.grid(column=0, row=1, sticky="new", padx=10, pady=10)
        dropdown_frame.columnconfigure(0, weight=1)
        dropdown_frame.rowconfigure(0, weight=0)
        dropdown_frame.rowconfigure(1, weight=0)
        self.tkvar = tkinter.StringVar(self.parent)
        self.tkvar.set('None')  # set the default option

        popupMenu = tkinter.OptionMenu(dropdown_frame, self.tkvar, *options)
        data_choice_label = tkinter.Label(dropdown_frame, text="Choose a datatype",
                                        bg="white", fg="black")
        data_choice_label.grid(row=0, column=0, sticky="nsew", padx=10)
        popupMenu.grid(row=1, column=0, sticky="nsew", padx=10)

        #self.tkvar.trace('w', self.change_dropdown)

    def makeform(self, fields):
        count=len(fields)
        entries = []
        lab_row_count = 0
        lab_column_count = 0
        ent_row_count = 0
        ent_column_count = 1
        entry_frame = tkinter.Frame(self.mainframe)
        entry_frame.grid(row=2, column=0, sticky="new", padx=10, pady=10)
        for field in fields:
            lab = tkinter.Label(entry_frame, text=field, anchor='w')
            lab.grid(row=lab_row_count, column=lab_column_count, sticky='ew')
            ent = tkinter.Entry(entry_frame)
            ent.grid(row=ent_row_count, column=ent_column_count, sticky='ew')
            lab_row_count += 1
            ent_row_count += 1

            #row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
            #lab.pack(side=tkinter.LEFT)
            #ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
            entries.append((field, ent))
        return entries

    def make_combobox(self, options):
        c_box = tttk.Combobox(self.parent, values=options)
        c_box.place(x=60, y=150)
        return
