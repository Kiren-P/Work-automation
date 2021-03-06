import tkinter as tk
from tkinter.constants import LEFT
from tkinter import filedialog
import os
from data import insert_paths, get_names, get_paths, save_current, get_current, delete

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
            folder = folder.replace("/", "\\")
            self.folder_path.insert("0", folder)

        def browseProgram(entry_x):
            entry_x.delete("0", "end")
            program = filedialog.askopenfile(mode="r", filetypes=[("Executables, Scripts, Etc...", "*.*")])
            abs_path = os.path.abspath(program.name)
            abs_path = abs_path.replace("/", "\\")
            entry_x.insert("0", abs_path)
        

        def Save():
            """Gets and saves paths for new preset"""
            folder = self.folder_path.get()
            program = self.path_to_program.get()
            program1 = self.path_to_program1.get()
            var3 = var.get()
            name = self.preset_name.get()
            insert_paths(folder, program, program1, var3, name)
            self.master.destroy()
            return start()

        #Add widgets

        #specify folder to open
        tk.Label(self.master, text="Specify the folder path:").grid(column=0, row=0, padx=2, sticky="NW")
        self.folder_path = tk.Entry(self.master, width=62)
        self.folder_path.grid(column=0, row=1, padx=2, sticky="NW")
        self.browse_folder = tk.Button(self.master, width=6, text="Browse", command=browseFolder)
        self.browse_folder.grid(column=1, row=1, padx=1, sticky="NW")

        #specify path to any other programs to run
        tk.Label(self.master, text="Path to program to run").grid(column=0, row=2, sticky="NW", padx=2, pady=2)
        self.path_to_program = tk.Entry(self.master, width=62)
        self.path_to_program.grid(column=0, row=3, sticky="NW", padx=2, pady=2 )
        self.browse_program = tk.Button(self.master, width=6, text="Browse", command=lambda :browseProgram(self.path_to_program))
        self.browse_program.grid(column=1, row=3, padx=1, sticky="NW")

        tk.Label(self.master, text="Path to second program to run").grid(column=0, row=4, sticky="NW", padx=2, pady=2)
        self.path_to_program1 = tk.Entry(self.master, width=62)
        self.path_to_program1.grid(column=0, row=5, sticky="NW", padx=2, pady=2 )
        self.browse_program1 = tk.Button(self.master, width=6, text="Browse", command=lambda :browseProgram(self.path_to_program1))
        self.browse_program1.grid(column=1, row=5, padx=1, sticky="NW")

        #radio button for cmd
        var = tk.IntVar()

        self.cmd_radio_1 = tk.Radiobutton(self.master, text="Open cmd", value=1, variable=var)
        self.cmd_radio_1.grid(column=0, row=6, padx=1, sticky="NW")
        self.cmd_radio_0 = tk.Radiobutton(self.master, text="Don't open cmd", value=0, variable=var)
        self.cmd_radio_0.grid(column=0, row=7, padx=1, sticky="NW")

        tk.Label(self.master, text="Select a name for this set of paths").grid(column=0, row=8, padx=2, pady=2, sticky="NW")
        self.preset_name = tk.Entry(self.master, width=62)
        self.preset_name.grid(column=0, row=9, padx=2, pady=2)
        
        self.save_button = tk.Button(self.master, text="Save", command=Save).grid(column=0, row=10, padx=2, pady=5)

        self.master.mainloop()

class Main:
    def __init__(self, master, title, geometry, height, width):
        self.master = master
        self.master.title(title)
        self.master.geometry(geometry)
        self.master.resizable(height=height, width=width)

        def new_preset():
            self.master.destroy()
            root = tk.Tk()
            window_size = "500x400"
            resizable_height = 0
            resizable_width = 0
            app = Menu(root, "Workflow Automation", window_size, resizable_height, resizable_width)
        
        def Confirm():
            """This confirms the chosen preset"""
            selected_preset = selected.get()
            save_current(selected_preset)
            return self.master.destroy()

        def deleteSelected():
            """This deletes the selected preset"""
            selected_preset = selected.get()
            delete(selected_preset)
            self.master.destroy()
            return start()
        
        #make a new preset
        self.new_preset_button = tk.Button(self.master, text="New preset", command=new_preset)
        self.new_preset_button.place(relx=0.5, rely=0.3, anchor="center")

        #select a preset
        selected = tk.StringVar()
        options = get_names()
        if len(options) == 0:
            options = ["No presets yet"]
            selected.set(options[0])
        else:
            selected.set(get_current())
        tk.Label(self.master, text="Select a preset").place(relx=0.5, rely=0.4, anchor="center")
        presets = tk.OptionMenu(self.master, selected, *options)
        presets.place(relx=0.5, rely=0.5, anchor="center")

        self.confirm_btn = tk.Button(self.master, text="Confirm", command=Confirm)
        self.confirm_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.delete_selected = tk.Button(self.master, text="Delete selected preset", command=deleteSelected)
        self.delete_selected.place(relx=0.5, rely=0.8, anchor="center")

        self.master.mainloop()

def start():
    root = tk.Tk()
    window_size = "200x300"
    resizable_height = 0
    resizable_width = 0
    app = Main(root, "Workflow Automation", window_size, resizable_height, resizable_width)


if __name__=="__main__":
    start()