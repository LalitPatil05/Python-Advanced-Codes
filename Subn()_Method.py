''' re.subn() method similiar to sub()method 
it returns or replace the string where match is founded/occurenced.
it returns the tuple of 2 items newString, No.of Substitution'''

import re

string = "Hello My Name is Python"
string2 = "HELLOPYTHON"

pattern = '\s+'

replace = "SPACE"

result = re.subn(pattern, replace, string)

result2 = re.subn(pattern,replace,string2)

result3 = re.subn(pattern, replace, string, 2)

print(result)

print(result2)

print(result3)
