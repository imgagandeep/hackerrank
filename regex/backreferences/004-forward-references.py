""" 
Forward reference creates a back reference to a regex that would appear later.
Forward references are only useful if they're inside a repeated group.
Then there may arise a case in which the regex engine evaluates the backreference after the group has been matched already.
Regex Pattern "(\2amigo|(go!))+" → Test String "go!go!amigo"

Task
You have a test string S.
Your task is to write a regex which will match S, with following condition(s):
→ S consists of tic or tac.
→ tic should not be immediate neighbour of itself.
→ The first tic must occur only when tac has appeared at least twice before.

Valid S
tactactic
tactactictactic

Invalid S
tactactictactictictac
tactictac

Note
This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r"^tac(tac(tic)?)*$"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
