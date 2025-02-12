'''
Demonstration of how to create the file using the write mode
it will be give the error if file already exist.
here we can pass the two parameters on open() function that is
open(newfilename.txt, 'r mode')
and using the write() function we can write the text into the file.
'''

file = open("newfile.txt","w")

file.write("This is a Sample text of new File\n")

file.write("Write mode allows to create a new file\n")

file.close()
