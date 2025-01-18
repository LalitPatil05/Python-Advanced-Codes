# Match object get methods and attributes .
# match.group() :- returns the part of string where there is a match.


import re


string = '39801 456, 2102 1111'

pattern = '(\d{3})(\d{2})'

result = re.search(pattern, string)

if result:
    print("Pattern Found")
    print(result)
else:
    print("Pattern Not Found")
