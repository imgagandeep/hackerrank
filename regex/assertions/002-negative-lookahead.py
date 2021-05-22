""" 
regex_1(?!regex_2)
The positive lookahead (?!) asserts regex_1 not to be immediately followed by regex_2. Lookahead is excluded from the match (do not consume matches of regex_2), but only asserts whether a match is possible or not.
Regex Pattern "c(!=o)" → Test String "chocolate"

Task
You have a test string S.
Write a regex which can match all characters which are not immediately followed by that same character.

Example
If S = goooo, then regex should match goooo. Because the first g is not follwed by g and the last o is not followed by o.

Note
This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"(\S)(?!\1)"	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
