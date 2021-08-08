#!/usr/bin/python3
"""Filter States"""

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

    query_1 = " SELECT states.id, name FROM states where name = '"
    query_2 = "' ORDER BY states.id ASC;"
    query_def = query_1 + state + query_2

    cursor = database.cursor()
    cursor.execute(query_def)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
