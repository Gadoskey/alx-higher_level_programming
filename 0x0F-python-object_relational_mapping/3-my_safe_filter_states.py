#!/usr/bin/python3
"""
A script that takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa` and makes it
safe from MySQL injections!

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    query = """
        SELECT *
        FROM states
        WHERE name LIKE BINARY %(name)s
        ORDER BY states.id ASC
    """
    cursor.execute(query, {'name': argv[4]})
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
