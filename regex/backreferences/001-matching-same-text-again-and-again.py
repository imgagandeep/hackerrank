""" 
\group_number
This tool (\1 references the first capturing group) matches the same text as previously matched by the capturing group.
Regex Pattern "(\w)(\w)(\w)(\w)y\4\3\2\1" → Test String "malayalam"

For Example:
(\d)\1: It can match 00, 11, 22, 33, 44, 55, 66, 77, 88 or 99.

Task
You have a test string S.
Your task is to write a regex that will match S with the following conditions:
→ S must be of length: 20
→ 1ˢᵗ character: lowercase letter.
→ 2ⁿᵈ character: word character.
→ 3ʳᵈ character: whitespace character.
→ 4ᵗʰ character: non word character.
→ 5ᵗʰ character: digit.
→ 6ᵗʰ character: non digit.
→ 7ᵗʰ character: uppercase letter.
→ 8ᵗʰ character: letter (either lowercase or uppercase).
→ 9ᵗʰ character: vowel (a, e, i , o , u, A, E, I, O or U).
→ 10ᵗʰ character: non whitespace character.
→ 11ᵗʰ character: should be same as 1st character.
→ 12ᵗʰ character: should be same as 2nd character.
→ 13ᵗʰ character: should be same as 3rd character.
→ 14ᵗʰ character: should be same as 4th character.
→ 15ᵗʰ character: should be same as 5th character.
→ 16ᵗʰ character: should be same as 6th character.
→ 17ᵗʰ character: should be same as 7th character.
→ 18ᵗʰ character: should be same as 8th character.
→ 19ᵗʰ character: should be same as 9th character.
→ 20ᵗʰ character: should be same as 10th character.

Note
This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
 """




# Solution:
Regex_Pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-z,A-Z][aieouAEIOU]\S)\1$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
