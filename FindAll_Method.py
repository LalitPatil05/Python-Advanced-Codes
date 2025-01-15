# re.findall() method returns the list of strings containing all maches

import re

string = 'hello 12 hi 89. World 34'
string2 = 'HELLO'
pattern = '\d+'

result = re.findall(pattern,string)
result2 = re.findall(pattern,string2)

print(result)
print(result2)
