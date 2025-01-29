# Demonstration of Search the Specific File into the Directory by using the os.listdir() method.
# give the path of this function by prefixed the r

import os

path = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder'

result = os.listdir(path)

for x in result:
    if(x.endswith(".txt")):
        print(x)
    else:
        print(x)
    
