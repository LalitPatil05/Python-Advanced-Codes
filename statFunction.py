'''
Demonstration of use of os.stat() function in python.
os.stat(file_path) function return all the information related to file
e.g id, size, ctime, mdtime, mode, ino, dev, uid, gid, etc.
'''

import os

filepath = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder\File1.txt'

result = os.stat(filepath)

print(result)
print(type(result))

