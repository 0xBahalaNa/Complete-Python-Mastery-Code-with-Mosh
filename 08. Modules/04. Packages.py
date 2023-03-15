"""
8. Modules, 04. Packages

As applications grow, developers should organize their directories.
Make an ecommerce subdirectory. 
Add sales.py to ecommerce folder.
Once module is moved, Python won't find sales.py.
Add a file __init__.py to the folder. 
The ecommerce folder is going to be a package. 
Packages is a container for one or more modules.
Package is mapped to a directory.
Module is mapped to a file.

Prefix the module with the directory.
To use any objects in the module, prefix with the package, then module. 
Use from statement to make it cleaner. 
Use from package, import module to make it even more easier.
"""
from ecommerce.sales import calc_tax
from ecommerce import sales
import ecommerce.sales

ecommerce.sales.calc_tax()
calc_tax()
