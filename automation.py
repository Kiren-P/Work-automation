import tkinter as tk
from tkinter.constants import LEFT
from tkinter import filedialog
import os
from data import insert_paths, get_paths

list_of_paths = get_paths()

if bool(list_of_paths):
    current_paths = list_of_paths[0]

    saved_folder = current_paths[0] 
    saved_cd_path = current_paths[1]
    saved_cmd_commands = current_paths[2]
    saved_other_program = current_paths[3]
else:
    saved_folder = False #this isn't the pyton way, find sth else to fix this
    saved_cd_path = False
    saved_cmd_commands = False
    saved_other_program = False

class Menu:
    def __init__(self, master, title, geometry, height, width):
        self.master = master
        self.master.title(title)
        self.master.geometry(geometry)
        self.master.resizable(height=height, width=width)

        #mehtods for wdigets
        def browseFolder():
            self.folder_path.delete("0", "end")
            folder = filedialog.askdirectory()
            self.folder_path.insert("0", folder)

        def browseProgram():
            self.path_to_program.delete("0", "end")
            program = filedialog.askopenfile(mode="r", filetypes=[("Executables, Scripts, Etc...", "*.*")])
            abs_path = os.path.abspath(program.name)
            self.path_to_program.insert("0", abs_path)

        def cdCurrentDirectory():
            return self.folder_path.get()

        def cdNewDirectory():
            self.new_directory = tk.Entry(self.master, width=62)
            self.new_directory.grid(column=0, row=4, sticky="NW", padx=2)

        def Save():
            """Gets paths"""
            folder = self.folder_path.get()
            try:
                cd_path = self.new_directory.get()
            except AttributeError:
                cd_path = self.folder_path.get()
            commands = self.cmd_commands.get("1.0", "end-1c")
            program = self.path_to_program.get()
            return insert_paths(folder, cd_path, commands, program)

        #Add widgets

        #specify folder to open
        tk.Label(self.master, text="Specify the folder path:").grid(column=0, row=0, padx=2, sticky="NW")
        self.folder_path = tk.Entry(self.master, width=62)
        self.folder_path.grid(column=0, row=1, padx=2, sticky="NW")
        self.browse_folder = tk.Button(self.master, width=6, text="Browse", command=browseFolder)
        self.browse_folder.grid(column=1, row=1, padx=1, sticky="NW")
        
        if saved_folder:
            self.folder_path.insert(0, saved_folder)

        #change directory to folder
        self.cdcurrent = tk.Button(self.master, text="Cd into specified folder", command=cdCurrentDirectory).grid(column=0, row=2, sticky="NW", padx=2, pady=2)
        self.cdnew = tk.Button(self.master, text="Specify new folder to cd in", command=cdNewDirectory).grid(column=0, row=3, sticky="NW", padx=2, pady=2)
        
        if saved_cd_path:
            if saved_cd_path == saved_folder:
                pass
            else:
                self.new_directory = tk.Entry(self.master, width=62)
                self.new_directory.grid(column=0, row=4, sticky="NW", padx=2)
                self.new_directory.insert(0, saved_cd_path)

        #specify commands to run
        tk.Label(self.master, text="Which cmd commands do you want to run?").grid(column=0, row=5, sticky="NW")
        self.cmd_commands = tk.Text(self.master, width=46, height=10)
        self.cmd_commands.grid(column=0, row=6, sticky="NW", padx=5, columnspan=2)
        if saved_cmd_commands:
            self.cmd_commands.insert("1.0", saved_cmd_commands)

        #specify path to any other programs to run
        tk.Label(self.master, text="Path to any other program to run (Not mentioned in cmd commands)").grid(column=0, row=7, sticky="NW", padx=2, pady=2)
        self.path_to_program = tk.Entry(self.master, width=62)
        self.path_to_program.grid(column=0, row=8, sticky="NW", padx=2, pady=2 )
        self.browse_program = tk.Button(self.master, width=6, text="Browse", command=browseProgram)
        self.browse_program.grid(column=1, row=8, padx=1, sticky="NW")
        if saved_other_program:
            self.path_to_program.insert(0, saved_other_program)

        #save button
        self.save_button = tk.Button(self.master, text="Save", command=Save).grid(column=0, row=10, padx=2)


        self.master.mainloop()


def run():
    root = tk.Tk()
    window_size = "500x400"
    resizable_height = 0
    resizable_width = 0
    app = Menu(root, "Workflow Automation", window_size, resizable_height, resizable_width)

if __name__=="__main__":
    run()