""" 
[^]
The negated character class [^] matches any character that is not in the square brackets.
Regex Pattern "[^aeiou] is not a vowel" → Test String "k is not a vowel, p is not a vowel"

Task
You have a test string S.
Your task is to write a regex that will match S with the following conditions:
→ S must be of length: 6
→ First character should not be a digit (1,2,3,4,5,6,7,8,9 or 0).
→ Second character should not be a lowercase vowel (a,e,i,o or u).
→ Third character should not be b, c, D or F.
→ Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
→ Fifth character should not be a uppercase vowel (A,E,I,O or U).
→ Sixth character should not be a . or , symbol.

Note

This is a regex only challenge. You are not required to write any code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
