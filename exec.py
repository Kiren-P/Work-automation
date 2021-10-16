import sqlite3
import os 


def get_and_run():
    con = sqlite3.connect("info.db")
    c = con.cursor()

    c.execute("""
    SELECT *
    FROM paths
    """)

    list_of_paths = c.fetchall()

    con.commit()
    con.close()

    paths = list_of_paths[0]
    print(paths)

    #use the os module to:
    saved_folder = paths[0] #open this folder
    saved_cd_path = paths[1] #cd into this folder
    saved_cmd_commands = paths[2] #execute these commands !!! (seperate them properly)
    saved_other_program = paths[3] #open this program


if __name__=="__main__":
    get_and_run()