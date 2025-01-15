# re.split() method split/skip the the string where match is found.

import re

string = 'Twelve:12EightyNine:89SixtyNine:69'
string2 = 'Twelve EightyNine SixtyNine'


pattern = '\d+'

result = re.split(pattern, string)
result2 = re.split(pattern, string2)

maxsplit = re.split(pattern, string, 1)


print(result)
print(result2)
print(maxsplit)

