import tkinter as tk
from tkinter.constants import LEFT

class Menu:
    def __init__(self, master, title, geometry):
        self.master = master
        self.master.title(title)
        self.master.geometry(geometry)

        #define methods for widgets 
        def browseButton():
            pass

        #Add widgets 

        #specify folder to open
        tk.Label(self.master, text="Specify the folder path:").grid(column=0, row=0, padx=2, sticky="NW")
        folder_path = tk.Entry(self.master, width=46).grid(column=0, row=1, padx=2)
        browse_button = tk.Button(self.master, widt=6, text="Browse", command=browseButton).grid(column=1, row=1, padx=2)


        #specify enviroment to activate 
        #specify commands to run
        #specify additional misc commands (usually project specific)



        self.master.mainloop()


def run():
    root = tk.Tk()
    window_size = "800x600"
    app = Menu(root, "Workflow Automation", window_size)

if __name__=="__main__":
    run()