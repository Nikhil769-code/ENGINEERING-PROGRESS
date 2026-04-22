import sys  
# sys:
# - Provides access to Python runtime environment
# - sys.path → list of directories Python searches for modules


# -------------------- Modifying Module Search Path --------------------

sys.path.append('/mnt/c/Users/Administrator/Desktop/My_module')
# Adds a new directory to Python's module search path
# Allows importing modules from this custom location


# NOTE:
# This change is temporary (only for current script/runtime)
# For permanent setup → use PYTHONPATH or install the module properly


# -------------------- Importing Custom Module --------------------

import my_module
# Python searches sys.path → finds module in appended directory → imports it


# IMPORTANT:
# If the module truly does not exist in any path → ImportError will occur
# It will NOT execute successfully if module is missing
