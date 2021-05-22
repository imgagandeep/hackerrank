""" 
(?|regex)
A branch reset group consists of alternations and capturing groups. (?|(regex1)|(regex2))
Alternatives in branch reset group share same capturing group.
Regex Pattern "(?|(Haa)|(Hee)|(bye)|(k))\1" → Test String "HaaHaa kk"

Task
You have a test string S.
Your task is to write a regex which will match S, with following condition(s):
→ S consists of 8 digits.
→ S must have "---", "-", "." or ":" separator such that string S gets divided in 4 parts, with each part having exactly two digits.
→ S string must have exactly one kind of separator.
→ Separators must have integers on both sides.

Valid S
12-34-56-78
12:34:56:78
12---34---56---78
12.34.56.78

Invalid S
1-234-56-78
12-45.78:10

Note
This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"^\d{2}(-(?:--)?|\.|:)\d{2}\1\d{2}\1\d{2}$"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
