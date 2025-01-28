'''
Another way to read a file is to call a certain number of characters
by using the file.read(range) function.
'''

file = open("demo.txt","r")

print(file.read(7))
