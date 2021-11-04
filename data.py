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

	c.execute("CREATE TABLE selected (selected_name TEXT UNIQUE)")

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
	connection.commit()
	connection.close()
	return names

def save_current(name):
	"""first deletes any previous saves and saves the selected preset name"""
	connection = sqlite3.connect("info.db")
	c = connection.cursor()
	c.execute("DELETE FROM selected")
	c.execute("INSERT INTO selected VALUES(?)", (name,))
	connection.commit()
	connection.close()
	return

def get_current():
	connection = sqlite3.connect("info.db")
	c = connection.cursor()
	c.execute("SELECT * FROM selected")
	name = [i[0] for i in c.fetchall()]
	try:
		name = name[0]
	except IndexError:
		name = "Nothing selected"
	connection.commit()
	connection.close()
	return name

def get_paths(name):
	"""Queries the preset of paths from paths table"""

	connection = sqlite3.connect("info.db")
	c = connection.cursor()

	c.execute("""
	SELECT *
	FROM paths
	WHERE name = (?)
	""", (name,))
	paths = c.fetchall()

	connection.commit()
	connection.close()
	return paths

def get_run():
    con = sqlite3.connect("info.db")
    c = con.cursor()
    c.execute("""
    SELECT folder_path, program, program2, cmd
    FROM paths
    INNER JOIN selected
    ON name = selected.selected_name
    """)
    list_of_paths = [i for i in c.fetchall()]
    con.commit()
    con.close()
    return list_of_paths

def delete(name):
	connection = sqlite3.connect("info.db")
	c = connection.cursor()
	if get_current() == name:
		c.execute("DELETE FROM selected")
	c.execute("DELETE FROM paths WHERE name = (?)", (name,))
	connection.commit()
	connection.close()
	return

def clear_tables():
	connection = sqlite3.connect("info.db")
	c = connection.cursor()
	
	c.execute("DELETE FROM paths")
	c.execute("DELETE FROM selected")

	connection.commit()
	connection.close()

