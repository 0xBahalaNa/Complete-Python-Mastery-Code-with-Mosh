"""
8. Modules, 03. Module Search Path

When a module is imported, Python will search for the module in the current directory.
In this example, it will look for sales.py.
Python will look in predefined directories that come with installation.
sys is a preinstalled module. 
.path will show the directory of the sys module. 
"""
import sales
import sys

print(sys.path)
