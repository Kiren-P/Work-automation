import tkinter as tk
from tkinter.constants import LEFT

class Menu:
    def __init__(self, master, title, geometry, height, width):
        self.master = master
        self.master.title(title)
        self.master.geometry(geometry)
        self.master.resizable(height=height, width=width)

        #mehtods for wdigets
        def browseButton():
            pass

        def cdCurrentDirectory():
            cmd_commands.insert(0.0, "cd " + "current path") # current path here

        def cdNewDirectory():
            new_directory = tk.Entry(self.master, width=62)
            new_directory.grid(column=0, row=4, sticky="NW", padx=2)

        def Save():
            """Saves the information to a database (or overrides existing info)"""
            folder = folder_path.get()
            #new_directory.get()
            commands = cmd_commands.get()
            program = path_to_program.get()
            pass

        #Add widgets 

        #specify folder to open
        tk.Label(self.master, text="Specify the folder path:").grid(column=0, row=0, padx=2, sticky="NW")
        folder_path = tk.Entry(self.master, width=62)
        folder_path.grid(column=0, row=1, padx=2, sticky="NW")
        browse_button = tk.Button(self.master, width=6, text="Browse", command=browseButton).grid(column=1, row=1, padx=1, sticky="NW")

        #change directory to folder
        tk.Button(self.master, text="Cd into specified folder", command=cdCurrentDirectory).grid(column=0, row=2, sticky="NW", padx=2, pady=2)
        tk.Button(self.master, text="Specify new folder to cd in", command=cdNewDirectory).grid(column=0, row=3, sticky="NW", padx=2, pady=2)

        #specify commands to run
        tk.Label(self.master, text="Which cmd commands do you want to run?").grid(column=0, row=5, sticky="NW")
        cmd_commands = tk.Text(self.master, width=46, height=10)
        cmd_commands.grid(column=0, row=6, sticky="NW", padx=5, columnspan=2)

        #specify path to any other programs to run
        tk.Label(self.master, text="Path to any other program to run (Not mentioned in cmd commands)").grid(column=0, row=7, sticky="NW", padx=2, pady=2)
        path_to_program = tk.Entry(self.master, width=62)
        path_to_program.grid(column=0, row=8, sticky="NW", padx=2, pady=2 )

        #save button
        tk.Button(self.master, text="Save", command=Save).grid(column=0, row=10, padx=2)

        self.master.mainloop()


def run():
    root = tk.Tk()
    window_size = "500x400"
    resizable_height = 0
    resizable_width = 0
    app = Menu(root, "Workflow Automation", window_size, resizable_height, resizable_width)

if __name__=="__main__":
    run()