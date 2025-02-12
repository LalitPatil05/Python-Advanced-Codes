'''
Demonstration of Create the new Directory of our system in Current working directory
or specified Location by using the os.mkdir() method.
'''

import os

print("Current Working Directory is :")
print(os.getcwd())
print(os.listdir())

os.mkdir('MyDirectory')

print("Directory Created Successfully..!!")

print("Curent Working Directory is : ")

print(os.getcwd())



