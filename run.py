import sqlite3
import os 
import webbrowser
from data import get_run



def run():
    paths = get_run()

    saved_folder = paths[0][0]
    program = paths[0][1]
    program1 = paths[0][2]
    cmd = paths[0][3]

    print(saved_folder, program, program1, cmd)
    #open alles
    webbrowser.open(saved_folder)
    # webbrowser.open(saved_other_program)
    # if open_cmd:
    #     webbrowser.open("C:\\WINDOWS\\system32\\cmd.exe")

    return


if __name__ == "__main__":
    run()