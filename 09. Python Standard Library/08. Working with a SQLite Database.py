"""
9. Python Standard Library, 08. Working with a SQLite Database

SQLite is a lightweight database.
Used for small applications like mobile.

Download DB Browser for SQLite.
"""
import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movies.values()))
    conn.commit()

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
        conn.commit()
    movies = cursor.fetchall()
    print(movies)
