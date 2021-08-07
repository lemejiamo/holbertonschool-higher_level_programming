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

	query = "SELECT states.id, name FROM states where name='" + state + "' ORDER BY states.id ASC;"
	cursor = database.cursor()
	cursor.execute(query)
	rows = cursor.fetchall()

	for row in rows:
	   print(row)

	cursor.close()
	database.close()
