##r'' or \\
##str = 'cd C:\Desktop\november\tab 在线试用'
##print(str)
##str = 'cd C:\Desktop\\november\\tab'
##print(str)
##regex. match()yes or none, search() show index from-to, findall()--list matches, sub()
##--replace return found sth or None
##[]--> like[sd] s or d ; [^not ] [a-zA-Z]==/S; [0-9]==\d !==\D; \s==empty spaces \slike\s== like
##\.
## $20 ->\$20
##. anycharacter; \w!==\W; --->e.*e; +== 1 or many or *==1 or many; ?==0 or 1 {6}=x6 times
## (man|woman); ^==beginning the line; $== end of the line
import re
reg = re.compile('\dstudents?')
result1 = reg.match('1students')
result2 = reg.search('121student1 22students 123student')
result3 = reg.findall('123student120students123student')
result4 = reg.sub( '搜狗输入法- 首页', '123student entsss ss12 3studen t123s tudent')
print(result1)
print(result2)
print(result3)
print(result4)
