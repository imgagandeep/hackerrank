""" 
Task
You are given a 2-D array of size NxM.
Your task is to find:
1. The mean along axis 1
2. The var along axis 0
3. The std along axis None

Input Format
The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format
First, print the mean.
Second, print the var.
Third, print the std.

Sample Input:
2 2
1 2
3 4

Sample Output:
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
 """




# Solution:
import numpy

n, m = map(int, input().strip().split())
a = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.mean(a, axis = 1))
print(numpy.var(a, axis = 0))
print(round(numpy.std(a, axis = None), 12))
