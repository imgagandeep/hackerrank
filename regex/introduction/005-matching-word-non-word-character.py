""" 
\w
The expression \w will match any word character.
Word characters include alphanumeric characters (a-z, A-Z and 0-9) and underscores (_).
Regex Pattern "\w\w\w" → Test String "$one"

\W
\W matches any non-word character.
Non-word characters include characters other than alphanumeric characters (a-z, A-Z and 0-9) and underscore (_).
Regex Pattern "\W" → Test String "$one"

Task
You have a test string S. Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here, x denotes any word character and X denotes non-word character.

Note
This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
