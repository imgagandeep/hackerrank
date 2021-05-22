""" 
^
The ^ symbol matches the position at the start of a string.
Regex Pattern "^123" → Test String "1235123"

$
The $ symbol matches the position at the end of a string.
Regex Pattern "123$" → Test String "1235123"

Task
You have a test string S. Your task is to match the pattern Xxxxx.
Here, x denotes a word character, and X denotes a digit.
S must start with a digit X and end with . symbol.
S should be 6 characters long only.

Note
This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"^\d\S{4}.$"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
