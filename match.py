import re

s = "python kxk 125"
# match 从头开始匹配
result = re.match("python", s)
print(result.span())  # (0, 6)
print(result.group())  # python

# search 全局匹配，匹配到第一个
s1 = "shd python ;sal;sfd"
result1 = re.search("python", s1)
print(result1.span())  # (4, 10)
print(result1.group())  # python

# findall 全局匹配，匹配到全部命中项
s2 = "shd python ;salpython;spythonfd"
result2 = re.findall("python", s2)
print(result2)  # ['python', 'python', 'python']

# 元字符匹配
"""
.   匹配任意1个字符(除了\n)，\.匹配点本身
[]  匹配[]中列举的字符
\d  匹配数字，即0-9
\D  匹配非数字
\s  匹配空白，即空格、tab键
\S  匹配非空白
\w  匹配单词字符，即a-2、A-Z、0-9、_
\W  匹配非单词字符
"""


# 匹配所有数字
s3 = "sfnam238%%%%$$$$$20-9sdm_"
result3 = re.findall(r'\d', s3) # 带r 标识转义无效  就是普通字符
print(result3) # ['2', '3', '8', '2', '0', '9']

# 找出特殊字符
result4 = re.findall(r'\W', s3)
print(result4) # ['%', '%', '%', '%', '$', '$', '$', '$', '$', '-']

# 找出全部英文字母
result4 = re.findall(r'[a-zA-Z]', s3)
print(result4) # ['s', 'f', 'n', 'a', 'm', 's', 'd', 'm']
