import sqlite3
import os 
import webbrowser

def get_and_run():
    con = sqlite3.connect("info.db")
    c = con.cursor()

    c.execute("""
    SELECT folder_path, program, program2, cmd
    FROM paths
    INNER JOIN selected
    ON name = selected.selected_name
    """)

    tuple_of_paths = c.fetchall()

    con.commit()
    con.close()

    print(tuple_of_paths)

    # #use the os module to:
    # saved_folder = paths[0] #open this folder
    # saved_other_program = paths[1] #open this program
    # open_cmd = paths[2]

    # webbrowser.open(saved_folder)
    # webbrowser.open(saved_other_program)
    # if open_cmd:
    #     webbrowser.open("C:\\WINDOWS\\system32\\cmd.exe")

    return


if __name__ == "__main__":
    get_and_run()