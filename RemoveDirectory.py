'''
Demonstration of How to Remove the Directory.
Using the os.remove() method to remove the file
Using the os.rmdir() method to remove the Directory
'''

import os

print("Current Working Directory is :")
print(os.getcwd())

print("List of File in Specified Directory :")
print(os.listdir())

os.rmdir( 'NewDirectory')
print("Directory is Successfully Deleted..!!")

print("After Removing File , the List is : ")
print(os.listdir())
