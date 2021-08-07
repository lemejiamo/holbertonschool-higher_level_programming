#!/usr/bin/python3
""" list all states from hbtn_0e_0_usa database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database_name)
    cursor = database.cursor()
    cursor.execute("SELECT states.id, name FROM states ORDER BY states.id ASC;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()

