""" 
dot
The dot (.) matches anything (except for a newline).
Regex Pattern "A.B.C.D." → Test String "A+B-C=DE"

Task
You have a test string S.
Your task is to write a regular expression that matches only and exactly strings of form: abc.def.ghi.jkx, where each variable a,b,c,d,e,f,g,h,i,j,k,x can be any single character except the newline.

Note
This is a regex only challenge. You are not required to write any code.
You only have to fill in the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"^...\....\....\....$"	# Do not delete 'r'.

import re
import sys
test_string = input()
match = re.match(regex_pattern, test_string) is not None
print(str(match).lower())
