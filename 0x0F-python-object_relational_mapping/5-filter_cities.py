#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
	username = argv[1]
	password = argv[2]
	database_name = argv[3]
	state = argv[4]
	database = MySQLdb.connect(host="localhost",
						 port=3306,
						 user=username,
						 passwd=password,
						 db=database_name)

	cursor = database.cursor()

	cursor.execute("""
		SELECT ct.name FROM cities AS ct
		JOIN states AS st
		ON ct.state_id=st.id
		where st.name = %(state)s
		ORDER BY ct.id;
	""", {
		'state': state
	})

	rows = cursor.fetchall()
	line = ""
	for row in rows:
	   line = line + row[0] + ', '
	
	print(line[0:-2])
	cursor.close()
	database.close()
