import sqlite3

#when this file runs the db will get created 

connection = sqlite3.connect("info.db")
c = connection.cursor()

def create_table():
	"""Creates a table with the columns"""

	c.execute("""CREATE TABLE paths (
			folder_path TEXT,
			cd_path TEXT,
			cmdcommands TEXT,
			programs TEXT 
			)""")

def insert_paths():
	"""Inserts paths into the paths table"""

	# c.execute("""
	# INSERT INTO paths 
	# VALUES (?, ?, ?, ?)""" ,(var1, var2, var3, var4)) these are the variables to be imported and inserted

def get_paths():
	"""Queries the all the paths from paths table"""

	c.execute("""
	SELECT *
	FROM paths
	""")
	paths = c.fetchall()


connection.commit()
connection.close()
