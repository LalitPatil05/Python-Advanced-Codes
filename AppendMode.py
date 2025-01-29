'''
Demonstration of how to add the new content in existing file by using the append mode
in which we can pass the two parameters for open() function ie. fileName and 'a' mode
and write the content to the file by using the write() function and this content are appended to
the end of the file. after complete the operation the main step is to close the file for termintates the
all the resources of system.
'''

file = open("newfile.txt", "a")

file.write("This Content Appended by Using the Append Mode in File Handeling\n")
file.write("Add this on End of the File\n")

file.close()
