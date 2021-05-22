""" 
Regular expression (or RegEx)
A regular expression is a sequence of characters that define a search pattern. It is mainly used for string pattern matching.
Regex Pattern "wikipedia" → Test String "https://en.wikipedia.org"

Task
You have a test string S. Your task is to match the string hackerrank. This is case sensitive.

Note
This is a regex only challenge. You are not required to write code.
You only have to fill in the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches: ", len(match))
