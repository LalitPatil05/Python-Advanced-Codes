'''
demonstration of how to overwritte into the file by using the write mode
we can give the two parameters of open() function i.e. open(filename,mode)
after complete the operation to close the file.

'''

file = open("newfile.txt", "w")

file.write("This Content are Append by Using the Write Mode\n")

file.close()
