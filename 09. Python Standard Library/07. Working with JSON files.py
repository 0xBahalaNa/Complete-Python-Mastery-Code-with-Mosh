"""
9. Python Standard Library, 07. Working with JSON Files

JSON = JavaScript Object Notation.
Popular way to format data in a human readable way.
Popular websites provide their data in JSON format.
Use pathlib and Path to write the data to a file. 
"""
import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 1, "title": "Kindergarten Cop", "year": 1993}
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
