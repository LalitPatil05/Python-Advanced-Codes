'''
There is more than one way to read a file in Python. If you need 
to extract a string that contains all characters in the file then we 
can use file.read().
'''

file = open("demo.txt","r") # pass the file name in open() function

print(file.read()) # access data using the read() function

