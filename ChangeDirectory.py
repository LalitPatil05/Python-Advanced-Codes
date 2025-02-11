'''
Demonstration of How to Change to Change the Position into one Directory to another
Directory by using the os.chdir(path)
'''

import os

print("Current Working Directorys is : ")

print(os.getcwd())

print("After Using chdir() Function Directory is :")
os.chdir(r'C:\\Users\\lalit\\Desktop\\TYBSC SEM-VI\\File Handeling Programs\\MyFolder\\')
print("Now the Current Directory is :")

print(os.getcwd())

print("Directory Changed Successfully...!!")
