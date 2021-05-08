""" 
Task
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format
The first line contains an integer N. M is the total number of integers in the list.
The second line contains the space separated list of N integers.

Constraints
0 < N < 100

Output Format
Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Sample Input:
5
12 9 61 5 14

Sample Output:
True

Explanation
Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

Hence, the output is True.

Can you solve this challenge in 3 lines of code or less?
There is no penalty for solutions that are correct but have more than 3 lines.
 """




# Solution:
n, item = int(input()), input().split()
print(all([int(i) > 0 for i in item]) and any([j == j[::-1] for j in item]))
