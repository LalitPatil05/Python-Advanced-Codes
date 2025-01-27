'''
Demonstration of How to Copy the files from one directory to another directory by using
the shutil module. shutil.copyfile() method in pythod is used to copy the content of source
directory to destination directory. metadata of the file is not copied.
'''
import os
import shutil

filepath=r'C:\Users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder'

print("Before Copying Files are : ")
print(os.listdir(filepath))

'''source_path = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder\NewFile.txt'

destination_path = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder\NewFilecopy.txt'

result = shutil.copyfile(source_path, destination_path)

print("After Copying the Files Are :")

print(os.listdir(path))

print("Destination Path is : ",result)'''





