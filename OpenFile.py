'''
To open a file for reading it is enough to specify the name of the file:
 f = open("demofile.txt")
 we can use the 'r' mode to read the content of the file.
 for loop we use to print the data of the file object
'''

file = open("demo.txt","r") # give the file name in open function 

for x in file:
    print(x) # access the file data on out application.
