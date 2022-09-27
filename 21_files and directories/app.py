# working with directories in python

from pathlib import Path

""" 
 Absolute path - C:\Program Files\Microsoft
            - /usr/local/bin

 Relative path

 path.mkidir() - creates a new directory
 path.rmdir() - deletes directory
 path.glob('*.*') - searches files
 path.glob('*') - searched for both files and directories
"""

# if you don't pass an argument, it will reference the current directory e.g.
path_one = Path()
print(path_one)

path_two = Path("tuples")
print(path_two.exists())

