#!/usr/bin/python3

"""
This script connects to a MySQL database
and lists all states where name matches
the argument.It takes 4 arguments:
MySQL username, password, and database name
state name searched.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database
        )

    cursor = mydb.cursor()

    query = ("SELECT * FROM states "
             "WHERE BINARY name = %s"
             "ORDER BY id ASC")

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    mydb.close()

