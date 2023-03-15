"""
9. Python Standard Library, 02. Working with Paths

Files and directories in Python. 
Import pathlib module and Path class.

https://docs.python.org/3/library/pathlib.html

Absolute paths.
Relative paths.

Path class has a lot of useful methods. 
Examples below. Use Python documentation to research what each method does.
"""


# Path(r"C\Program Files\Microsoft")
path = Path(
    r"/Users/luigi/Desktop/Coding/Code with Mosh/Python/9. Python Standard Library")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path.with_name
