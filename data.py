import sqlite3

connection = sqlite3.connect("paths.db")

c = connection.cursor()

c.execute("""CREATE TABLE paths (
        folder_path text,
        cd_path text,
        email text 
        )""")

connection.commit()
connection.close()

#COLUMNS: FOLDER PATH, PATH TO CD IN, COMMANDS TO RUN. PATH TO EXTRA PROGRAM