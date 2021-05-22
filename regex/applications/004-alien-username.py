""" 
In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:
1. It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
2. The first character must be immediately followed by one or more digits in the range 0 through 9.
3. After some number of digits, there must be 0 or more English letters (uppercase and/or lowercase).
4. It may be terminated with an optional _ (ASCII value 95). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of 0 or more English letters.

Given n strings, determine which ones are valid alien usernames. If a string is a valid alien username, print VALID on a new line; otherwise, print INVALID.

Input Format
The first line contains a single integer, n, denoting the number of usernames.
Each line i of the n subsequent lines contains a string denoting an alien username to validate.

Constraints
→ 1 ≤ n ≤ 100

Output Format
Iterate through each of the n strings in order and determine whether or not each string is a valid alien username. If a username is a valid alien username, print VALID on a new line; otherwise, print INVALID.

Sample Input
3
_0898989811abced_
_abce
_09090909abcD0

Sample Output
VALID
INVALID
INVALID

Explanation
We validate the following three usernames:
1. _0898989811abced_ is valid as it satisfies the requirements specified above. Thus, we print VALID.
2. _abce is invalid as the beginning _ is not followed by one or more digits. Thus, we print INVALID.
3. _09090909abcD0 is invalid as the sequence of English alphabetic letters is immediately followed by a number. Thus, we print INVALID.
 """




# Solution:
import re

regex = re.compile('^[_\.][0-9]+[a-zA-Z]*[_]?$')
n = int(input())
for i in range(n):
    string = str(input())
    if (len(re.findall(regex, string)) != 0):
        print("VALID")
    else:
        print("INVALID")
