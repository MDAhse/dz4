from typing import Optional, Match

text = open("text.txt","r")
import re
helpp = text.readline()
result = re.sub(r'\?|\!','.', helpp)
a = 1

result = re.split(r'[\n\.]', result)
text1 = open("text1.txt", "w")
for i in result:
    result1 = re.search(r'^\D.+$', str(result))
    result1 = re.sub(r'^', str(a), str(result1))
    a+=1
    text1.write(result1)
text.close()
text1.close()


