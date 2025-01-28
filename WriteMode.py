''''
Demonstration of How to Write Into Existing file.
By Using the write mode we can override the new content into file.
'''

file = open("newfile.txt", "w")

file.write("New Content of File\n")

file.close()
