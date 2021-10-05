import tkinter as tk
from tkinter.constants import LEFT

class Menu:
    def __init__(self, master, title, geometry):
        self.master = master
        self.master.title(title)
        self.master.geometry(geometry)

            
        #mehtods for wdigets
        def browseButton():
            pass

        def cdCurrentDirectory():
            pass

        def cdNewDirectory():
            new_directory = tk.Entry(self.master, width=46).grid(column=0, row=4, sticky="NW", padx=2)

        #Add widgets 

        #specify folder to open
        tk.Label(self.master, text="Specify the folder path:").grid(column=0, row=0, padx=2, sticky="NW")
        folder_path = tk.Entry(self.master, width=46).grid(column=0, row=1, padx=2)
        browse_button = tk.Button(self.master, widt=6, text="Browse", command=browseButton).grid(column=1, row=1, padx=2)

        #change directory to folder
        tk.Button(self.master, text="Cd into specified folder", command=cdCurrentDirectory).grid(column=0, row=2, sticky="NW", padx=2, pady=2)
        tk.Button(self.master, text="Specify new folder to cd in", command=cdNewDirectory).grid(column=0, row=3, sticky="NW", padx=2, pady=2)

        #specify commands to run
        tk.Label(self.master, text="Which cmd commands do you want to run?").grid(column=0, row=5, sticky="NW")
        cmd_commands = tk.Text(self.master, width=45, height=10).grid(column=0, row=6, sticky="NW", padx=5, columnspan=3)

        self.master.mainloop()


def run():
    root = tk.Tk()
    window_size = "800x600"
    app = Menu(root, "Workflow Automation", window_size)

if __name__=="__main__":
    run()