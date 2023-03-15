"""
9. Python Standard Library, 05. Working with Zip Files

https://docs.python.org/3/library/zipfile.html

Use zipfile module and import ZipFile class.
Useful for working with zip files.
Read, write, read/write.
Extract files
"""
from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    for path in Path("r/Users/luigi/Desktop/Coding/Code with Mosh/Python/9. Python Standard Library").rglob("*.*"):
        zip.write(path)
zip.close()

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
