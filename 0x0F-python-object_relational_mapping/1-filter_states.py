#!/usr/bin/python3
"""
File: 1-filter_states.py
Author Onyejekwe Philip
Desc: A script that lists states with a name starting with N
        from the database hbtn_0e_0_usa.
Date: 17 aug 2023
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                    WHERE BINARY name LIKE 'N%' ORDER BY id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
