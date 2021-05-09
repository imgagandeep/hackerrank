""" 
Task
You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.

Input Format
A single line of input containing 9 space separated integers.

Output Format
Print the 3x3 NumPy array.

Sample Input:
1 2 3 4 5 6 7 8 9

Sample Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 """




# Solution:
import numpy as np

a = np.array(list(map(int, input().split())))
a.shape = (3, 3)
print(a)
