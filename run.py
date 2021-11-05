import sqlite3
import os 
import webbrowser
from data import get_run



def run():
    paths = get_run()

    saved_folder = paths[0][0]
    program = paths[0][1]
    program1 = paths[0][2]
    open_cmd = paths[0][3]

    webbrowser.open(saved_folder)
    webbrowser.open(program)
    webbrowser.open(program1)
    if open_cmd:
        webbrowser.open("C:\\WINDOWS\\system32\\cmd.exe")

    return


if __name__ == "__main__":
    run()