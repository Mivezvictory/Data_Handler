import tkinter as tk


class V_ScrollableFrame_Sample(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior_frame' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)


        """ 
         Create a canvas object; specify the border thickness, specify the highlight thickness.
         The border thickness and highlight thickness are 0 in this case because the borders should not be visible.
         We do not need to show the borders, since another frame will simply be placed within in. 
         It is necessary that the canvass and this frame cannot be differentiated from each other.
         Pack the contents of the canvass to the left, let it fill all the way from left to right.
         Allow the canvass to expand."""
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a vertical scrollbar that will be used to scroll through the canvas created above.
        # Force it to the right side.
        self.v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.v_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.v_scrollbar.config(command=self.canvas.yview)

        # Assign the vertical scroll bar to control the canvas.
        self.canvas.config(yscrollcommand=self.v_scrollbar.set)

        # Create a frame as a window inside the canvas, so that it can be scrolled with the canvass' scrollbar.
        # Get the id of the frame so that it can be used to readjust the size, and anchor it to the North-west position.
        self.interior_frame = tk.Frame(self.canvas, bg="black")
        self.interior_frame_id = self.canvas.create_window(0, 0, window=self.interior_frame, anchor=tk.NW)

        # Bind the interior frame and canvas to their respective functions.
        # These will adjust their sizes according to the changes that occur on the UI.
        self.interior_frame.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)

    def _configure_interior(self, event):
        """Track changes to the  width and height of the canvas and frame and sync them."""
        # Update the scrollbars to match the size of the inner frame.
        """The .winfo_reqwidth() and .winfo_reqheight() functions are used to get the required dimensions needed 
        to show the objects widgets based on the changes, to the window size."""
        size = (self.interior_frame.winfo_reqwidth(), self.interior_frame.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)

        # If the required width is different from the current width make changes.
        if self.interior_frame.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width=self.interior_frame.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.interior_frame.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_frame_id, width=self.canvas.winfo_width())


