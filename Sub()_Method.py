# re.sub() method returns or replace the string where match is founded/occurenced.

import re

string = "Hello My Name is Python"
string2 = "HELLOPYTHON"

pattern = '\s+'

replace = "SPACE"

result = re.sub(pattern, replace, string)

result2 = re.sub(pattern,replace,string2)

result3 = re.sub(pattern, replace, string, 2)

print(result)

print(result2)

print(result3)
