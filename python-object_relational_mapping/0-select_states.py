#!/usr/bin/python3

"""
This script connects to a MySQL database
and lists all states from the 'states' table,
ordered by 'id'. It takes three arguments:
MySQL username, password, and database name.
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    mydb.close()
