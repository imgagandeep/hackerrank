""" 
{x}
The tool {x} will match exactly x repetitions of character/character class/groups.
Regex Pattern "\w{4}" → Test String "H_ck"

For Example:
w{3} : It will match the character w exactly 3 times.
[xyz]{5} : It will match the string of length 5 consisting of characters {x, y, z}. For example it will match xxxxx, xxxyy and xyxyz.
\d{4} : It will match any digit exactly 4 times.

Task
You have a test string S.
Your task is to write a regex that will match S using the following conditions:
→ S must be of length equal to 45.
→ The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
→ The last 5 characters should consist of odd digits or whitespace characters.

Note
This is a regex only challenge. You are not required to write any code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
