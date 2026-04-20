import os
from datetime import datetime 

os.chdir('/mnt/c/Users/Administrator/Desktop/JP/Python/Modules/')
# Changes the current working directory


# -------------------- Directory Creation --------------------

os.mkdir('Temp_dir')  
# Creates a single directory (fails if it already exists)

os.makedirs('temp_dir/sub_dir')  
# Creates nested directories (creates parent if needed)

# NOTE:
# On Windows (case-insensitive filesystem), 'Temp_dir' and 'temp_dir'
# are treated as the SAME directory.
# So this results in: Temp_dir/sub_dir
# On Linux/macOS (case-sensitive), these would be separate directories.


# -------------------- Directory Deletion --------------------

os.rmdir('Temp_dir')  
# Removes a single directory (must be empty)

os.removedirs('Temp_dir/sub_dir')  
# Removes nested directories (removes sub_dir, then Temp_dir if empty)


# -------------------- Current Working Directory --------------------

print(os.getcwd())  
# Prints current working directory


# -------------------- File Operations --------------------

os.rename('demo.txt','test.txt')  
# Renames a file


# -------------------- File Metadata --------------------

mod_time = os.stat('test.txt').st_mtime  
# st_mtime → returns float (Unix timestamp)

print(datetime.fromtimestamp(mod_time))  
# Converts timestamp → human-readable datetime


# -------------------- Directory Traversal --------------------

for dirpath, dirnames, filenames in os.walk('/mnt/c/Users/Administrator/Desktop/JP/Python/Modules/'):
    print('Current Path : ', dirpath)
    print('Directories : ', dirnames)
    print('Files : ', filenames)
    print()

# os.walk():
# - Generator that yields (dirpath, dirnames, filenames)
# - Traverses directory tree recursively


print(os.listdir())  
# Lists files and directories in current directory


# -------------------- Environment Variables --------------------

print(os.environ.get('HOME'))  
# Gets value of HOME environment variable
# (Use os.environ to see all variables)


# -------------------- Path Handling --------------------

file_path = os.path.join(os.environ.get('HOME'), 'demo.txt')
print(file_path)  
# Safely joins paths (OS-independent)


print(os.path.basename('/tmp/test.txt'))  
# Extracts filename → 'test.txt'

print(os.path.dirname('/tmp/text.txt'))  
# Extracts directory path → '/tmp'

print(os.path.split('txt/text.txt'))  
# Splits into (directory, filename)


# -------------------- Path Checks --------------------

print(os.path.exists('/tmp/test.txt'))  
# Checks if path exists

print(os.path.exists('/home/nikhilgoswami'))

print(os.path.isdir('/home/nikhilgoswami'))  
# True if path is a directory

print(os.path.isfile('/home/nikhilgoswami'))  
# True if path is a file


# -------------------- File Extension --------------------

print(os.path.splitext('/tmp/test.txt'))  
# Splits into ('/tmp/test', '.txt')