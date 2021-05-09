""" 
Task
You are given a 2-D array with dimensions NxM. Your task is to perform the tool over axis 0 and then find the product of that result.

Input Format
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format
Compute the sum along axis 0. Then, print the product of that sum.

Sample Input:
2 2
1 2
3 4

Sample Output:
24

Explanation
The sum along axis 0 = [4 6]
The product of this sum = 24
 """




# Solution:
import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))
