#!/usr/bin/python3
'''
This module takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
'''
import MySQLdb
import sys


if __name__ == "__main__":

    if len(sys.argv) != 5:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states "
                   "WHERE name = '{}' "
                   "ORDER BY id ASC".format(state_name))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
