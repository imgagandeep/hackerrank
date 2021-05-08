""" 
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

Input Format
A single line of input consisting of the string S.

Output Format
A single line of output consisting of the modified string.

Constraints
All the characters of S denote integers between 0 and 9.
1 ≤ |S| ≤ 10⁴

Sample Input:
1222311

Sample Output:
(1, 1) (3, 2) (1, 3) (2, 1)
 """




# Solution 1:
from itertools import groupby

n = input()
print(* [(len(list(a)), int(b)) for b, a in groupby(n)])



# Solution 2:
# for key, group in groupby(input()):
#     print((len(list(group)), int(key)), end=' ')
