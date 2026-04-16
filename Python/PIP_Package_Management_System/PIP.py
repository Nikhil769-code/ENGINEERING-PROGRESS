# PIP PACKAGE MANAGEMENT SYSTEM --- The pip commands run in terminal 

# pip list  = Lists all the installed packages in Python

# pip list -o = Lists all the outdated packages with their current and newer versions 

# pip install -u pkg_name  = Updates a single package to its latest version 

# pip list --outdated --format=freeze | cut -d = -f | xargs -n1 pip install -U       = This command checks for all outdated packages and updates them one by one 

# pip freeze =  Outputs all the packages in Python along with their version numbers in a requirements format 

# pip freeze > requirements.txt     = Copies the freeze output to the text file (Usually used to send someone the list of packages used in project)

# pip install -r requirements.txt  = Installs all the packages from requirements file 

