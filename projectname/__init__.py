"""
projectname
==================================
Add library description here...

Author: Casokaks (https://github.com/Casokaks/)
Created on: Aug 15th 2021

"""

# -----------------------------------------------------------------------------------
# Library version
# -----------------------------------------------------------------------------------
__version__ = "0.3.1"

# -----------------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------------
from .module import *  # The General Store: expose all modules, functions, attributes in projectname
from .module import placeholder  # The Convenience Store: expose only selected objects in projectname 
import projectname.module  # [RECOMMENDED] Online grocery shopping: expose only modules in projectname 
