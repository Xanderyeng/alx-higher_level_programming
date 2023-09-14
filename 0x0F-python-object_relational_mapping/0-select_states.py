#!/usr/bin/python3
"""
    Write a script that lists all states from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states ORDER BY states.id")
    names = cur.fetchall()
    for item in names:
        print(item)
    cur.close()
    db.close()
