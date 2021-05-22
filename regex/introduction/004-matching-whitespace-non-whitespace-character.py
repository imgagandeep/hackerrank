""" 
\s
\s matches any whitespace character [ \r\n\t\f ].
Regex Pattern "\s" → Test String "A B"

\S
\S matches any non-white space character.
Regex Pattern "\S" → Test String "A B"

Task
You have a test string S. Your task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters, and X denotes non-white space characters.

Note
This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
