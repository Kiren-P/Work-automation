import tkinter as tk

class Menu:
    def __init__(self, master, title, geometry):
        self.master = master
        self.master.title(title)
        self.master.geometry(geometry)

        #define methods for widgets 

        #Add widgets 
        Label = tk.Label(self.master, text="Hello World")
        Label.pack()



        self.master.mainloop()

def run():
    root = tk.Tk()
    app = Menu(root, "Workflow Automation", "800x600")

if __name__=="__main__":
    run()