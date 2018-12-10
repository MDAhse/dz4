from typing import Optional, Match

text = open("text.txt","r")
import re
helpp = text.readline()
result = re.sub(r'\?|\!','.', helpp)
a = 1

result = re.split(r'\.', result)
text1 = open("text1.txt", "w")

for i in range(0,len(result)-1):
    text1.write(str(i+1))
    text1.write(result[i]+'\n')

text.close()
text1.close()
