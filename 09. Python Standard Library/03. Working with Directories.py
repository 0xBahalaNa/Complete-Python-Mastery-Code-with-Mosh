"""
9. Python Standard Library, 03. Working with Directories

Can use Path class with directories.
Methods are similar to Linux/Mac commands.

https://docs.python.org/3/library/pathlib.html

iterdir lists all files and directories in path. 
Produces a generator object.
Iterable.

Can use list comprehension.
Returns array of Posix path objects.
Posix is for Unix like OSs.
Has two limitations:
1. Can't search by pattern.
2. Can't search recursively.

To search by pattern prefix with "*".
To search recursively use rglob.
"""
from pathlib import Path

# path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

path = Path(
    r"/Users/luigi/Desktop/Coding/Code with Mosh/Python/9. Python Standard Library")

# print(path.iterdir())

# for p in path.iterdir():
#     print(p)

# print([p for p in path.iterdir() if p.is_dir])

print([p for p in path.glob("*.py")])
print([p for p in path.rglob("*.py")])
