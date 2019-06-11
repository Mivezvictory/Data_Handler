import Tkinter
from UI import DataEntry


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.title("Better than Metadata Wizard")
    DataEntry.DataEntry(root)
    root.mainloop()
