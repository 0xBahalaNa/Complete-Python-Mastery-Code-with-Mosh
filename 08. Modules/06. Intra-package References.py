"""
8. Modules, 06. Intra-package References

Import modules from sibling packages. 
Absolute or relative import.
Best practice is use absolute.
Absolute import is the first line.
If absolute import name is verbose, use relative import. 
"""
from ecommerce.customer import contact
from ..customer import contact

contact.contact_customer()
