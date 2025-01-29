'''
Demonstration of How to Rename the File
Rename the file from old name to new name
using the os.rename(source_file, destination_file)
in which we can give the source file name as existing name of file and destination file name as a
new name of file 
'''

import os

source_path = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder\OldFile.txt'

destination_path =  r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder\NewFile.txt'

os.rename(source_path, destination_path)

print("File Renamed Successfully...!!")

