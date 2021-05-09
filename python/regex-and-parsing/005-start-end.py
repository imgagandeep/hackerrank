""" 
Task
You are given a string S. Your task is to find the indices of the start and end of string k in S.

Input Format
The first line contains the string S.
The second line contains the string k.

Constraints
0 < len(S) < 100
0 < len(k) < len(S)

Output Format
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input:
aaadaa
aa

Sample Output:
(0, 1)  
(1, 2)
(4, 5)
 """




# Solution:
import re

string = input()
substring = input()
pattern = re.compile(substring)
match = pattern.search(string)
if not match:
    print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() -1))
    match = pattern.search(string, match.start() + 1)
