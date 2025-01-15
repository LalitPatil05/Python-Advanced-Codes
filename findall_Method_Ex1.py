import re

string = 'Hello2World'

pattern = '\d+'

result = re.findall(pattern, string)

print(result)
