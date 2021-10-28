import sqlite3

def create_table():

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""CREATE TABLE paths (
		folder_path TEXT,
		program TEXT,
		cmd INTEGER,
		name TEXT
		)""")

	connection.commit()
	connection.close()

def insert_paths(var1, var2, var3, var4):
	"""Inserts paths into the paths table"""

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""
	INSERT INTO paths 
	VALUES (?, ?, ?, ?)""" ,(var1, var2, var3, var4))

	connection.commit()
	return connection.close()

def get_paths():
	"""Queries the all the paths from paths table"""

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""
	SELECT *
	FROM paths
	""")
	paths = c.fetchall()

	connection.commit()
	connection.close()
	return paths

create_table()