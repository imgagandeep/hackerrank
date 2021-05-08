""" 
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition.
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
→ Print the three most common characters along with their occurrence count.
→ Sort in descending order of occurrence count.
→ If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G,O,E.

Input Format
A single line of input containing the string S.

Constraints
→ 3 < len(S) ≤ 10⁴

Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input:
aabbbccde

Sample Output:
b 3
a 2
c 2

Explanation 0
aabbbccde
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
Note: The string S has at least 3 distinct characters.
 """




# Solution:
import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = sorted(input().strip())
    s_count = collections.Counter(s).most_common()
    s_count = sorted(s_count, key= lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(s_count[i][0], s_count[i][1])
