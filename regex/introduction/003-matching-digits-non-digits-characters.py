""" 
\d
The expression \d matches any digit [0-9].
Regex Pattern "\d\d\d." → Test String "HACK101"

\D
The expression \D matches any character that is not a digit.
Regex Pattern "\D\D\D." → Test String "HACK101"

Task
You have a test string S. Your task is to match the pattern xxXxxXxxxx
Here x denotes a digit character, and X denotes a non-digit character.

Note

This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"\d\d(.)\d\d(.)\d\d\d\d"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
