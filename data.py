import sqlite3

def create_table():

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""CREATE TABLE paths (
		folder_path TEXT,
		program TEXT,
		program2 TEXT,
		cmd INTEGER,
		name TEXT,
		UNIQUE(name)
		)""")

	connection.commit()
	connection.close()

def insert_paths(var1, var2, var3, var4, var5):
	"""Inserts paths into the paths table"""

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""
	INSERT INTO paths (folder_path, program, program2, cmd, name)
	VALUES (?, ?, ?, ?, ?)""" ,(var1, var2, var3, var4, var5))

	connection.commit()
	connection.close()
	return

def get_names():
	""" returns all the preset names"""
	connection = sqlite3.connect("info.db")
	c = connection.cursor()
	c.execute("SELECT name FROM paths")
	names = [i[0] for i in c.fetchall()]
	return names


def get_paths():
	"""Queries the preset of paths from paths table"""

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

def clear_table():
	connection = sqlite3.connect("info.db")
	c = connection.cursor()
	
	c.execute("DELETE FROM paths")

	connection.commit()
	connection.close()
