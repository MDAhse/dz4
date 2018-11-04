text = open("text.txt","r")
import re
helpp = text.readline()
result = re.sub(r'\?|\!','.', helpp)
a = 1
result = re.sub(r'\.','[\.\n]', result)
for i in result:
    result1 = re.sub(r'^', str(a), result)
    a+=1
text1=open("text1.txt", "w")
text1.write(result1)
text.close()
text1.close()


