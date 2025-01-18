# Match object get methods and attributes .
# match.re() :- it returns the Regular Expression Object.


import re


string = '39801 356, 2102 1111'

pattern = '(\d{3})(\d{2})'

result = re.search(pattern, string)

if result:
    print("Pattern Found")
    print(result.group())
    print(result.groups())
    print(result.re)
else:
    print("Pattern Not Found")
