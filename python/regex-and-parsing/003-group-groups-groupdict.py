""" 
Task
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

Input Format
A single line of input containing the string S.

Constraints
0 < len(S) < 100

Output Format
Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input:
..12345678910111213141516171820212223

Sample Output:
1

Explanation
.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
 """




# Solution:
import re

m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)
