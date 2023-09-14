#!/usr/bin/python3
"""
 script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!
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
    cur.execute("SELECT * FROM states WHERE states.name\
                LIKE BINARY %s ORDER BY states.id", (state, ))
    names = cur.fetchall()
    for item in names:
        print(item)
    cur.close()
    db.close()
