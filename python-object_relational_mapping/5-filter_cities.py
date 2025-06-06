#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state using the database hbtn_0e_4_usa.
This version prevents SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    db.close()
