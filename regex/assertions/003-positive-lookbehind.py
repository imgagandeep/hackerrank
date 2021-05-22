""" 
(?<=regex_2)regex_1
The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2. Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
Regex Pattern "(?<=[a-z])[aeiou]" → Test String "he1o"

Task
You have a test String S.
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.

Note
This is a regex only challenge. You are not required to write a code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"(?<=[13579])[0-9]"	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
