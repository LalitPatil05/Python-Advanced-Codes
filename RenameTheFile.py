'''
Demonstration of How to Rename the File Using File Handeling in Python.
os.rename method to rename the File
'''

import os

print(os.getcwd())

print("Before Rename The File Name is ")
print()
print(os.listdir())
print("After Rename The File Name is ")
print()
os.rename('Demo.txt','NewDemo.txt')
print("File Renamed Successfully...!!")
print(os.listdir())

