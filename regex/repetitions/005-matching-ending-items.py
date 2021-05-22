""" 
$
The $ boundary matcher matches an occurrence of a character/character class/group at the end of a line.
Regex Pattern "\w*s$" → Test String "Challenges Hints"

Task
Write a RegEx to match a test string, S, under the following conditions:
→ S should consist of only lowercase and uppercase letters (no numbers or symbols).
→ S should end in s.

This is a RegEx-only challenge, so you are not required to write any code.
Simply replace the blank (_________) with your RegEx pattern.
 """




# Solution:
Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
