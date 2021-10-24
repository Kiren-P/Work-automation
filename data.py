import sqlite3

def create_table():

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""CREATE TABLE paths (
		folder_path TEXT,
		program TEXT,
		cmd INTEGER 
		)""")

	connection.commit()
	connection.close()

def insert_paths(var1, var2, var3):
	"""Inserts paths into the paths table
	(The table only has one record, the current one)"""

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	#deletes any previous records 
	c.execute("DELETE FROM paths")

	c.execute("""
	INSERT INTO paths 
	VALUES (?, ?, ?)""" ,(var1, var2, var3))

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
