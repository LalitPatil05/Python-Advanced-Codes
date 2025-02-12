'''
Demonstration of how to get the information about the current working directory
os.getcwd() function return the current working directory in form of string
 a getcwdb() method return the info it as bytes object
'''

import os

print("Path in String :")
print(os.getcwd())

print("Path in Byte :")
print(os.getcwdb())
