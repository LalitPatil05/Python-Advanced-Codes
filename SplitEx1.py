import re

string = '1Hello2World3'

pattern = '\d+'

result = re.split(pattern, string)

print(result)
