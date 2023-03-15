"""
9. Python Standard Library, 04. Working with Files

Path class to work with files.

https://docs.python.org/3/library/pathlib.html

Use time module for time related classes and methods.
shutil for shell utilities. 
"""
from pathlib import Path
from time import ctime
import shutil

path = Path(
    r"/Users/luigi/Desktop/Coding/Code with Mosh/Python/9. Python Standard Library")
target = Path((
    r"/Users/luigi/Desktop/Coding/Code with Mosh/Python/9. Python Standard Library"))
shutil.copy(path, target)
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(ctime(path.stat().st_ctime))

path.read_bytes()
path.read_text()

with open("__init__.py", "r") as file:
    ...

path.write_text("...")
path.write_bytes()
