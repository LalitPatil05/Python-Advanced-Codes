'''
Demonstration of os.listdir() method
this method returns the all files and directories in a specified directory
in which this function give the directory path by prefix the r to search the files
this function return the list of files.

'''

import os

path = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder'

result = os.listdir(path)

print(result)

