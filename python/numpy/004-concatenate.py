""" 
Task
You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

Input Format
The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format
Print the concatenated array of size (N + M) x P.

Sample Input:
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Sample Output:
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
 """




# Solution:
import numpy as np

a, b, c = map(int, input().split())
arr1 = np.array([input().split() for _ in range(a)], int)
arr2 = np.array([input().split() for _ in range(b)], int)
print(np.concatenate((arr1, arr2), axis = 0))
