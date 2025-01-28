'''
Obtain Information about the file in python
  os.path.getsize() returns the size of the file
  os.path.getmtime() returns the file last modified date
  os.path.getctime() returns the file creation date
 Using This Functions we can Get the More Information about the File.
'''
import os
from datetime import datetime
filepath = r'c:\users\lalit\desktop\TYBSC SEM-VI\File Handeling Programs\MyFolder\File1.txt'
size = os.path.getsize(filepath)
modified = os.path.getmtime(filepath)
create = os.path.getctime(filepath)

epoch_m_time = modified
formatted_m_time = datetime.fromtimestamp(epoch_m_time)
epoch_c_time = create
formatted_c_time = datetime.fromtimestamp(epoch_c_time)

print("File Size is : ",size)
print("Modified Time of File is : ",formatted_m_time.strftime('%d-%m-%y %H:%M:%S'))
print("Creation Time of File is : ",formatted_c_time.strftime('%d-%m-%y %H:%M:%S'))
