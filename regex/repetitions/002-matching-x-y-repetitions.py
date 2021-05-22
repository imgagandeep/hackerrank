""" 
{x, y}
The {x,y} tool will match between x and y (both inclusive) repetitions of character/character class/group.
Regex Pattern "\w{1,4}\d{4,}" → Test String "Hk132156153186131 Hack1021"

For Example:
w{3,5} : It will match the character w 3, 4 or 5 times.
[xyz]{5,} : It will match the character x, y or z 5 or more times.
\d{1, 4} : It will match any digits 1, 2, 3, or 4 times.

Task
You have a test string S.
Your task is to write a regex that will match S using the following conditions:
→ S should begin with 1 or 2 digits.
→ After that, S should have 3 or more letters (both lowercase and uppercase).
→ Then S should end with up to 3. symbol(s). You can end with 0 to 3. symbol(s), inclusively.

Note
This is a regex only challenge. You are not required to write any code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
