#!/usr/bin/python3
"""
    Write a script that lists all states starting with "N" from
    the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
arg = sys.argv


if __name__ == "__main__":
    if len(arg) > 4:
        print("Usage: ./0-select_states.py username password database")
    db = MySQLdb.connect(
        host="localhost",
        user=arg[1],
        passwd=arg[2],
        db=arg[3],
        port=3306)
    cur = db.cursor()
    cur.execute("SELECT DISTINCT cities.id, cities.name, states.name\
                 FROM cities INNER JOIN states ON cities.state_id = states.id\
                 ORDER BY cities.id ASC")
    names = cur.fetchall()
    for item in names:
        print(item)
    cur.close()
    db.close()
