""" 
In this challenge, you will be given 2 integers, n and m.  There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each  words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. 
If it does not appear, print -1.

Constraints
1 ≤ n ≤ 10000
1 ≤ m ≤ 100
1 ≤ length of each word in the input ≤ 100

Input Format
The first line contains integers, n and m separated by a space. 
The next n lines contains the words belonging to group A. 
The next m lines contains the words belonging to group B.

Output Format
Output m lines. 
The iᵗʰ line should contain the 1-indexed positions of the occurrences of the iᵗʰ word separated by spaces.

Sample Input:
5 2
a
a
b
a
b
a
b

Sample Output:
1 2 4
3 5

Explanation
'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
 """




# Solution:
from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(d[input()]) or -1)
