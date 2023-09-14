#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys
arg = sys.argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=arg[1],
        passwd=arg[2],
        db=arg[3],
        port=3306)
    state = arg[4]
    cur = db.cursor()
    i = 1

    count = cur.execute("SELECT cities.name FROM cities WHERE state_id = ( \
                        SELECT id \
                        FROM states \
                        WHERE name LIKE BINARY %s) \
                        ORDER BY cities.id ASC", (state, ))
    names = cur.fetchall()
    for item in names:
        print(item[0], end="")
        if i < count:
            print(end=", ")
            i += 1
    print()
    cur.close()
    db.close()
