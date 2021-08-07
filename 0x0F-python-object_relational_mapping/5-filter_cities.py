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
		SELECT states.id new_table.name
		JOIN states AS new_table
		ON cities.id=new_table.id
		where new_table.name = %(state)s
		ORDER BY new_table.name ASC;
	""", {
		'state': state
	})

	rows = cursor.fetchall()

	for row in rows:
	   print(row)

	cursor.close()
	database.close()
