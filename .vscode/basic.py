# Boolean, Numbers, String, Bytes, Lists, Tuples, Sets, Dictionaries ...
a="string"
b=True
c=10
d= 10.1
dic= {
    "name":"kim",
    "age":10
}
llist=[3,4,5]
ttuple=4,5,6
sset={4,5,6}
print(type(sset))

# +,-,*,/,//,%,**.....
# > >= < <= == != +=.....

# 형변환 int,float,complex,str.....
print(int(d))

# math 함수
import math
print(math.ceil(5.1))
print(math.floor(3.456))

#문자열
str1="hello"
str2="python"
str3=\
"""ha
ha
ha"""

print(len(str1))
print(str1+"\t"+str2)
print(str3)

print('h' in str1)
print('h' not in str1)

# 문자열함수...

str10="nice"
print(str10.islower())
print(str10.lower())
print(str10.isupper())

print(str10[0:2])