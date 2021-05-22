""" 
regex_1(?=regex_2)
The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2. The lookahead is excluded from the match. It does not return matches of regex_2.
The lookahead only asserts whether a match is possible or not.
Regex Pattern "c(?=o)" → Test String "chocolate"

Task
You have a test string S.
Write a regex that can match all occurrences of o followed immediately by oo in S.

Note
This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
