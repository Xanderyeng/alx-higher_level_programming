#!/usr/bin/python3
"""
Module for script that takes an argument and displays all value in the
states table where name matches the argument
"""


import sys
import MySQLdb

if __name__ == "__main__":
    name = sys.argv[4]
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cur = db.cursor()

    sql_cmd = "SELECT * FROM states WHERE name='{}' ORDER BY id;".format(name)
    cur.execute(sql_cmd)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
