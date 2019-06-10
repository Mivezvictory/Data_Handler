import tkinter
from UI import DataEntry


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Better than Metadata Wizard")
    DataEntry.DataEntry(root)
    root.mainloop()
